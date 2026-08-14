#!/usr/bin/env python3
"""Restartable VascX A/V inference for a directory of fundus images."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import torch
from rtnls_fundusprep.cli import _run_preprocessing
from rtnls_inference.ensembles.ensemble_segmentation import SegmentationEnsemble


def device() -> torch.device:
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def chunks(items: list[Path], size: int):
    for start in range(0, len(items), size):
        yield items[start:start + size]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--weights", type=Path, default=Path("../third_party/vascx_weights/av_july24.pt"))
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--chunk-size", type=int, default=128)
    parser.add_argument("--preprocess-jobs", type=int, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--save-logits", action="store_true", help="Also save ensemble-mean pre-softmax logits.")
    args = parser.parse_args()

    files = sorted(path for path in args.images.glob("*") if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".ppm", ".tif", ".tiff"})
    if args.limit is not None:
        files = files[:args.limit]
    if not files:
        raise SystemExit(f"No images found in {args.images}")
    args.output.mkdir(parents=True, exist_ok=True)
    rgb_dir, ce_dir, av_dir, logits_dir = (
        args.output / name for name in ("preprocessed_rgb", "preprocessed_ce", "artery_vein", "logits")
    )
    for directory in (rgb_dir, ce_dir, av_dir, logits_dir):
        directory.mkdir(parents=True, exist_ok=True)

    missing_preprocess = [
        path for path in files
        if not (rgb_dir / f"{path.stem}.png").is_file() or not (ce_dir / f"{path.stem}.png").is_file()
    ]
    if missing_preprocess:
        _run_preprocessing(
            files=missing_preprocess,
            ids=[path.stem for path in missing_preprocess],
            rgb_path=rgb_dir,
            ce_path=ce_dir,
            bounds_path=args.output / "bounds_latest_batch.csv",
            n_jobs=args.preprocess_jobs,
        )

    missing = [
        path for path in files
        if not (av_dir / f"{path.stem}.png").is_file()
        or (args.save_logits and not (logits_dir / f"{path.stem}.npy").is_file())
    ]
    if missing:
        runtime_device = device()
        model = SegmentationEnsemble.from_torchscript(args.weights).to(runtime_device).eval()
        for group in chunks(missing, args.chunk_size):
            entries = [
                {
                    "id": path.stem,
                    "image": str(rgb_dir / f"{path.stem}.png"),
                    "contrast_enhanced": str(ce_dir / f"{path.stem}.png"),
                }
                for path in group
            ]
            hard_entries = [entry for entry in entries if not (av_dir / f"{entry['id']}.png").is_file()]
            if hard_entries:
                model.predict_preprocessed(
                    hard_entries, dest_path=av_dir, num_workers=0, batch_size=args.batch_size
                )
            if args.save_logits:
                logit_entries = [entry for entry in entries if not (logits_dir / f"{entry['id']}.npy").is_file()]
                model.predict_logits_preprocessed(
                    logit_entries, dest_path=logits_dir, num_workers=0,
                    batch_size=args.batch_size, dtype=np.float16,
                )
            if runtime_device.type == "mps":
                torch.mps.synchronize()
                torch.mps.empty_cache()
            elif runtime_device.type == "cuda":
                torch.cuda.empty_cache()
    print(f"complete images={len(files)} predictions={len(list(av_dir.glob('*.png')))}")


if __name__ == "__main__":
    main()
