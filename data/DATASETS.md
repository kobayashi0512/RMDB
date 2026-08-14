# Dataset registry and redistribution policy

This registry separates analysis provenance from redistribution permission. A dataset being downloadable does not automatically make it lawful or appropriate to mirror.

| Dataset | Role in RMDB | Original source | Licence or access | Mirrored in release |
|---|---|---|---|---|
| China Fundus CIMT | CIMT development and frozen evaluation resource | Springer Nature Figshare article 27907056 | CC0 | Yes |
| FIVES | vessel occupancy development | Figshare article 19688169 | CC BY 4.0 | Yes |
| Fundus AVSeg | locked external artery and vein measurement test | Figshare article 27938034, version 2 | CC BY 4.0 | Yes |
| AFIO | external artery and vein and vessel structure audit | Mendeley Data DOI 10.17632/3csr652p9y.2 | CC BY 4.0 | Yes |
| RAV | frozen VascX audit and separate development resource | DataverseNL DOI 10.34894/9OIMWY | CC BY NC 4.0 | Yes, noncommercial use only |
| Fundus DG OD OC | optic disc domain resource | Zenodo DOI 10.5281/zenodo.8009107 | CC BY 4.0 | Yes |
| NHANES | feasibility and metadata audit | United States CDC NHANES | public government release; component documentation applies | Yes |
| STARE | structure migration audit | STARE project site | no sufficiently explicit redistribution licence was found in the local copy | No; obtain from the original source |
| mBRSET | exploratory repeatability and clinical association | PhysioNet DOI 10.13026/qxpd-1y65 | credentialed access, required training, and data use agreement | **No** |
| MESA and ARIC metadata probes | access feasibility only | official cohort portals | controlled access | **No** |

## Important boundary

The mBRSET image and metadata files must be obtained by each authorized researcher from PhysioNet. They must not be reconstructed from the release, redistributed to another account, or treated as open data. This repository includes only aggregate, nonpatient level results from that branch.

## Integrity

`OPEN_DATA_ASSETS_SHA256.txt` records the exact release assets. After download, verify an asset with:

```bash
shasum -a 256 -c OPEN_DATA_ASSETS_SHA256.txt
```

Attribution and citation remain required even when a copy is provided for reproducibility.

