# Reassembling large release assets

Three archives are split into numbered release assets to make the upload resilient. Most parts are 95 MiB. The FIVES segment numbered `part006` is represented by ten smaller files named `part006.subpart-aa` through `part006.subpart-aj`; this avoids a stalled single-connection upload. Download every listed file, verify it against the part manifest, then concatenate files with the same archive prefix in lexical order.

```bash
shasum -a 256 -c LARGE_ASSET_PARTS_SHA256.txt

cat RMDB_model_checkpoints_v1.0.0.tar.gz.part* > RMDB_model_checkpoints_v1.0.0.tar.gz
cat China_Fundus_CIMT_CC0.tar.gz.part* > China_Fundus_CIMT_CC0.tar.gz
cat FIVES_CC_BY_4.0.zip.part* > FIVES_CC_BY_4.0.zip

shasum -a 256 -c MODELS_AND_LARGE_ARCHIVES_SHA256.txt
```

The numbered suffix is zero padded, and the FIVES subparts sort between `part005` and `part007`, so ordinary lexical expansion preserves the original byte order. There is intentionally no release asset named exactly `FIVES_CC_BY_4.0.zip.part006`. Do not extract an archive until its reconstructed SHA256 matches the manifest.
