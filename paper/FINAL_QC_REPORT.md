# Final scientific and presentation audit

Date: 14 August 2026

## Scope checked

The main manuscript, supplementary appendix, editable figure deck, figure captions, tables, equations, cohort roles, exact reported estimates, and source manifest were checked together.

## Corrections completed

1. Figure 1 now shows seven real retinal image resources and their prespecified roles. RAV is identified as a frozen VascX audit plus a separate UDCT development resource. Fundus AVSeg is identified as the locked external UDCT test.
2. Figure 2 uses a distinct real CIMT development image and shows anatomy standardization, dual readouts, phenotype construction, the BiRAP reliability gate, patient aggregation, and the stopping rule.
3. Figure 3 now pairs a real RAV photograph, reference mask, and frozen VascX output with a different real Fundus AVSeg photograph, reference mask, and locked Mass UDCT output. The transport panel reports five cohorts rather than four.
4. Figure 4 reports the exact repeatability experiment using 2,359 same eye pairs and the four of nine retained phenotypes.
5. Figure 5 is described as a two panel figure and matches the CIMT development and frozen validation ladder.
6. Figure 6 is described as a three panel figure and separates calibrated mBRSET increments, permutation integrity control, and the final claim boundary.
7. Table 1 now separates development, measurement, reliability, transport, clinical, and access audit roles. Tables 2 and 3 report exact estimates and prespecified decisions without overstating clinical confirmation.

## Equation audit

Five equations were retained because each is needed to reproduce a distinct method component:

1. the two step UDCT residual logit update;
2. the implemented archived UDCT training loss, including the 0.20 artery and vein mass term and the 0.05 total vessel mass term;
3. the fixed confidence and occupancy gate with threshold 0.525;
4. the interpretable mass, artery and vein balance, and readout disagreement operators;
5. cross fitted normative deviation and double orthogonalization.

The former standalone reliability indicator equation was removed because Algorithm 1 already states the exact ICC threshold. No decorative or unused formula remains.

## Language and typography audit

Ordinary prose was rewritten to avoid ASCII hyphenation. Remaining ASCII hyphens occur only in protected names and identifiers such as Fundus AVSeg, Mass UDCT, E8 B, E8 D, bibliographic titles and DOI strings, or in necessary negative numerical signs. Scientific artery–vein relations use an en dash.

All 23 main manuscript pages and all 5 supplementary pages were rendered and inspected. The editable six slide figure deck passed the automated overflow test.

All 20 references are cited in the main text. Methodological references are attached to the ICC, bootstrap, clinical prediction, reporting, correlated ROC, and VascX passages in which they are actually relevant.

## Claim boundary

The completed evidence supports external pixel measurement and outcome blind repeatability. It shows that phenotype scales are not directly exchangeable across cohorts. Conditional CIMT deviation remains exploratory. Stable clinical incremental value and independent high resolution outcome confirmation are not established.

## Author supplied items still required

Author names, affiliations, corresponding author details, ethics and consent wording, funding, competing interests, author contributions, and any repository accession chosen for submission remain explicit placeholders and must be supplied by the authors.
