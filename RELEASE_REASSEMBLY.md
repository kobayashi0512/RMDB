# Reassembling large release assets

Three archives are split into numbered 95 MiB release assets to make the upload resilient. Download every part with the same prefix, verify the parts, then concatenate them in lexical order.

```bash
shasum -a 256 -c LARGE_ASSET_PARTS_SHA256.txt

cat RMDB_model_checkpoints_v1.0.0.tar.gz.part* > RMDB_model_checkpoints_v1.0.0.tar.gz
cat China_Fundus_CIMT_CC0.tar.gz.part* > China_Fundus_CIMT_CC0.tar.gz
cat FIVES_CC_BY_4.0.zip.part* > FIVES_CC_BY_4.0.zip

shasum -a 256 -c MODELS_AND_LARGE_ARCHIVES_SHA256.txt
```

The numbered suffix is zero padded, so ordinary lexical expansion preserves the original byte order. Do not extract an archive until its reconstructed SHA256 matches the manifest.

