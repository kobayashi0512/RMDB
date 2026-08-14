# RMDB--BiRAP manuscript completion queue

This queue runs the missing analyses serially and resumes from non-empty output markers.

1. Audit prior CIMT split access without opening raw validation/test rows.
2. Extend the four-feature repeatability evidence with ICC, SEM, MDC95, within-subject CV, and Bland--Altman limits.
3. Run locked-OOF outcome permutation and random-eye-pairing negative controls.
4. Add calibration, calibration uncertainty, and exploratory decision curves for overall, no-DR, and strict-disc-QC analyses.
5. Build cohort, participant-flow, fair-comparison, and secondary-outcome tables from frozen artifacts.
6. Audit label-blind transport of the four reliable phenotypes across mBRSET, RAV, and Fundus-AVSeg.
7. Test whether measured QC overlap weighting can explain the cross-cohort phenotype shifts, with prespecified balance and ESS gates.
8. Preflight an independent high-resolution external cohort. Missing external data is recorded as `BLOCKED_EXTERNAL_DATA` and does not become a false validation claim.
9. Compile the completion summary.

Formal run:

```bash
.venv-vascx/bin/python scripts/run_manuscript_completion_queue.py
```

Smoke run:

```bash
.venv-vascx/bin/python scripts/run_manuscript_completion_queue.py --quick --force
```

Status and logs are written under `artifacts/manuscript_completion/`.

External cohort contract:

- Set `RMDB_EXTERNAL_COHORT_DIR`, or place data in `external_validation/MESA/data/`.
- Provide `manifest.csv` with `patient_id,image_id,eye,image_path,age,sex,cimt_mm`.
- Provide original high-resolution images in `images/`.
- External model execution remains frozen and must follow `external_validation/MESA_一次性外部验证锁定协议.md`.
- A blocked external-data marker is not treated as completion: rerunning the queue after the cohort is supplied automatically retries step 06.
