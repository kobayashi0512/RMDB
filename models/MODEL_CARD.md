# RMDB model card

## Intended purpose

The archived models support research reproduction of vessel occupancy, artery and vein readouts, bilateral CIMT baselines, phenotype construction, and negative control experiments. They are not approved clinical models.

## Model families

1. Bilateral and multimodal fundus baselines.
2. Clinical residual and demographic debiasing experiments.
3. FIVES vessel occupancy segmentation.
4. UDCT and factorized artery and vein readouts.
5. BIMFO pilot and outer cross validation checkpoints.

## Evidence gate

Pixel performance alone is not accepted as biomarker validity. Downstream phenotypes are retained only after the prespecified repeatability and reliability audit described in Algorithm 1 of the manuscript.

## Limitations

The checkpoints were created for the exact preprocessing and cohort roles documented in the repository. They must not be interpreted as validated diagnostic tools. Stable clinical incremental value and independent high resolution outcome confirmation have not been established.

## Distribution

Checkpoint binaries are attached to the repository release as `RMDB_model_checkpoints_v1.0.0.tar.gz`. `MODEL_ASSETS_SHA256.txt` records both the archive checksum and the checksum of each checkpoint contained in it.

