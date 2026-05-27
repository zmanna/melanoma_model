# Model Governance

## Intended Use

Current intended use is limited to education, technical demonstration, and internal evaluation of a melanoma image-classification workflow.

The model may be used to study:

- image upload and inference mechanics
- CNN training and evaluation
- model documentation patterns
- health-adjacent AI risk management
- product diligence for medical AI concepts

## Not Intended For

This model must not be used for:

- medical diagnosis
- clinical screening
- treatment decisions
- triage
- patient reassurance
- emergency guidance
- autonomous recommendations
- handling protected health information
- production deployment

## Model Output

The model returns a single sigmoid-style score. The app currently converts that score to:

- `Malignant`
- `Benign`

This output should be treated as a raw experimental classifier score, not calibrated confidence and not medical probability.

## Evaluation Standard For Future Work

A serious model-governance process should require:

- fixed dataset manifests
- train/validation/test split provenance
- external validation data
- demographic performance analysis
- device and image-quality sensitivity analysis
- confusion matrices by cohort
- recall and false-negative analysis
- calibration analysis
- threshold selection rationale
- model-card updates for every released model
- human clinical review

## Risk Priorities

| Risk | Concern |
|---|---|
| False negative | User may be falsely reassured. |
| False positive | User may experience unnecessary anxiety or cost. |
| Dataset bias | Performance may vary across skin tones, devices, lighting, and lesion types. |
| Distribution shift | Consumer uploads may differ greatly from training images. |
| Overclaiming | Product language can imply clinical validity that does not exist. |
| Privacy | Uploaded images may be sensitive or identifying. |

## Governance Gate

No model should be promoted from prototype to product candidate until these questions are answered:

1. What exact data trained it?
2. What exact data evaluated it?
3. What is the legally permitted use of that data?
4. What threshold is used and why?
5. How does performance vary by subgroup and image source?
6. What is the intended clinical workflow?
7. Who is accountable for reviewing the output?
8. What regulatory pathway applies?

