# RMDB

RMDB is a reproducible retinal microvascular digital biomarker framework developed to test a simple but often overlooked proposition: good pixel segmentation is not the same as a valid, transportable biomarker.

The repository accompanies the manuscript **“Pixel Accuracy Is Not Biomarker Validity: RMDB–BiRAP, a Framework with Dual Readouts and Reliability Gating for Retinal Vascular Phenotyping Across Domains.”** The current complete manuscript is `paper/RMDB_3.1_Complete_FiguresIntegrated.docx`. Earlier manuscript and figure iterations are retained under `paper/history/` for provenance.

## What RMDB contains

RMDB standardizes fundus anatomy, obtains two deliberately nonidentical vascular readouts, constructs interpretable vascular phenotypes, and applies a repeatability gate before clinical association testing. The central BiRAP rule retains only phenotypes with adequate same eye repeatability and stops unsupported branches instead of repeatedly tuning them against outcomes.

The evidence chain has three distinct layers:

1. **Measurement validity:** external artery and vein segmentation and vessel occupancy evaluation.
2. **Cross domain reliability:** repeatability, quality gating, and five cohort phenotype transport audits.
3. **Clinical association:** patient level nested evaluation in the CIMT development setting and exploratory mBRSET analyses, with permutation controls and explicit claim boundaries.

The current evidence supports external pixel measurement and four repeatable vascular phenotypes. It does **not** establish exchangeable phenotype scales across cohorts, stable clinical incremental value, or independent high resolution outcome confirmation.

## Repository map

| Path | Contents |
|---|---|
| `paper/` | Current manuscript RMDB 3.1, original RMBD 1.0 deposit, supplement, current editable figures, source manifests, and complete manuscript and figure history |
| `src/` | Project source code used for training, phenotype extraction, validation, sensitivity analysis, and manuscript generation |
| `configs/` | Frozen data and experiment configuration files |
| `protocols/` | Locked protocols, negative result records, decision logs, and paper blueprints |
| `evidence/` | Aggregate evidence tables and figures that do not contain patient level predictions |
| `data/` | Dataset registry, licence notes, official acquisition links, and asset checksums; raw data are distributed only when their licences permit it |
| `models/` | Model card and checkpoint manifest; checkpoint binaries are attached to the GitHub release |

## Reproduction

Create a clean environment and install the pinned top level dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verify the dataset registry before running an experiment:

```bash
python src/check_rmdb_data.py
```

The individual scripts expose command line help. The locked protocols in `protocols/` specify the permitted cohort role, split, endpoint, threshold, and stopping rule for each experiment. Do not use the fixed CIMT validation or test subsets for new model selection.

## Data and model assets

Open datasets are archived as release assets only when their original licence permits redistribution. mBRSET is not mirrored because PhysioNet classifies it as a credentialed, data use agreement controlled resource. See `data/DATASETS.md` for the exact provenance and restrictions.

Model checkpoints and the two largest open datasets are stored as numbered release parts rather than Git blobs. Every part and reconstructed archive has a SHA256 entry in the release manifests. See `RELEASE_REASSEMBLY.md` for the exact reconstruction commands.

The `v3.1.0-archive` release adds the complete V2 and V3 optimisation outputs and the open-data reverse-validation outputs generated from 21 to 26 August 2026. These archives contain logs, configurations, metrics, derived maps, and experiment checkpoints. They do not contain credentialed mBRSET images or patient-level controlled-access tables. See `ARCHIVE_20260827.md` and `RELEASE_20260827_SHA256.txt`.

## Responsible use

RMDB is a research framework, not a medical device. It is not intended for diagnosis, treatment selection, or autonomous cardiovascular screening. External clinical confirmation is still required before any clinical claim.

## Citation

Citation metadata are provided in `CITATION.cff`. Until peer review is complete, cite the repository version and the accompanying draft.

## Licence and third party components

No blanket relicensing of third party datasets, pretrained weights, or dependencies is implied. Each dataset and dependency remains under its original terms. Project source is currently shared for research review in this private repository; an explicit public source licence should be selected before making the repository public.
