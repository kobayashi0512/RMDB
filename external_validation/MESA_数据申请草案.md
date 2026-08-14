# MESA 数据/合作申请草案

## Project title

External validation of a retinal microvascular digital biopsy for
age- and sex-conditional carotid intima-media thickness deviation

## Brief objective

We aim to externally validate a fully locked retinal image analysis pipeline that
converts bilateral color fundus photographs into interpretable microvascular
phenotypes and estimates carotid intima-media thickness (CIMT) relative to the
expected value for participants of the same age and sex. The study is intended
as a screening/triage investigation and will not claim that fundus photography
replaces carotid ultrasonography.

## Primary cohort requested

MESA Exam 5 participants with:

1. de-identified raw retinal photographs;
2. same-exam continuous carotid IMT measurements;
3. age and sex;
4. a stable de-identified participant key for patient-level linkage.

Exam 2 retinal photographs and the nearest available CIMT examination are
requested only for prespecified temporal-gap sensitivity analyses.

The current dbGaP distribution manifest appears to list phenotype tables rather
than JPEG/TIFF image files for the Exam 2 and Exam 5 retinal photography
datasets. We therefore specifically request confirmation of whether archived
de-identified image pixels can be provided through a MESA collaboration or a
separate approved image-transfer mechanism.

## Requested retinal data

- Raw de-identified image pixels, not thumbnails;
- both eyes where available;
- Field 1 (disc-centered) as required;
- Field 2 (macula/fovea-centered) as optional secondary input;
- laterality and field indicator;
- acquisition date/exam number;
- camera/site information if available;
- photo completeness and gradability;
- reasons for missing/ungradable images;
- existing CRAE/CRVE and retinal pathology grades for mechanism/QC analyses.

## Requested carotid data

- Continuous left/right common carotid far-wall mean IMT;
- maximum IMT if available;
- bulb/internal carotid measurements if available;
- the study-defined overall/mean CIMT used in MESA publications;
- scan/reading quality, missingness and protocol flags;
- ultrasound examination date;
- plaque variables as secondary outcomes only.

Completion-status variables alone are not sufficient; continuous thickness
measurements in millimetres are required.

## Requested covariates

Required:

- age at retinal examination;
- sex;
- race/ethnicity;
- field centre;
- retinal and carotid examination dates.

Secondary, for descriptive and sensitivity analyses only:

- smoking;
- systolic/diastolic blood pressure;
- diabetes;
- antihypertensive and lipid-lowering medication;
- BMI;
- lipids;
- prior cardiovascular disease.

The primary incremental analysis will remain restricted to age and sex so that
it matches the locked development model.

## Frozen analysis

- No MESA participant will be used for model development or threshold selection.
- The China Fundus-CIMT model, image preprocessing, feature list and two output
  heads will be frozen before MESA pixels are read.
- H0 is the conditional-mean head and is evaluated with RMSE/R²/calibration.
- H1 is the conditional-percentile robust head and is evaluated with MAE,
  accelerated-CIMT discrimination and worst-group error.
- The previous head-disagreement score will not be treated as uncertainty.
- Confidence intervals will use patient-level bootstrap resampling.
- Results will be reported overall and by sex, age, race/ethnicity, field centre
  and image quality, subject to disclosure limits.

## Data security

All controlled data will be stored and analysed in an institution-approved
access-controlled environment. Identifiers will not be re-identified or linked
outside the approved datasets. Raw data will not be redistributed. Access,
retention, reporting and destruction will follow the executed DUA and MESA/dbGaP
requirements.

## Information still required before submission

- applicant PI name and position;
- institution and department;
- institutional email;
- eRA Commons credentials for dbGaP, if that path is used;
- IRB/ethics determination or exemption status;
- approved secure computing/storage description;
- proposed project dates and personnel;
- institutional signing official.

Submitting the form or sending this text externally requires explicit approval
after the above institutional information is supplied.
