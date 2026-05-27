# Model Card

## Model Summary

| Field | Value |
|---|---|
| Task | Binary image classification |
| Classes | Benign, malignant |
| Framework | TensorFlow/Keras |
| Interface | Flask web app |
| Input shape | `256x256` RGB image |
| Output | Probability-like model score converted to a class label |
| Project status | Academic prototype |
| Clinical status | Not clinically validated |

## Intended Use

This model is intended for educational demonstration of image classification workflows. It is not intended for medical use, clinical screening, diagnosis, treatment decisions, triage, or patient-facing deployment.

## Not Intended For

- medical diagnosis
- replacing professional clinical judgment
- use with private patient images
- HIPAA-regulated workflows
- production deployment
- automated health recommendations

## Data

The project acknowledges the International Skin Imaging Collaboration (ISIC) as the dataset source. Any future documentation pass should specify the exact dataset subset, download date, preprocessing split, and license terms used during training.

## Preprocessing

- Images are resized to `256x256`.
- Pixel values are normalized from `[0, 255]` to `[0, 1]`.
- Directory names provide binary labels during training.

## Decision Thresholds

The repository currently contains multiple threshold references:

| Location | Threshold |
|---|---:|
| Flask runtime in `backend/app.py` | `0.4` |
| Training parameters in `model/model_parameters.json` | `0.35` |
| Evaluation script in `model/test_model.py` | `0.5` |
| Historical tracker note in `docs/melanoma_model_tracker.md` | `0.7` |

These values should be aligned before making any final statement about model behavior. Until then, threshold-dependent metrics should be interpreted as iteration artifacts rather than stable model claims.

## Evaluation Considerations

The documentation discusses accuracy, precision, recall, F1 score, confusion matrix behavior, false positives, and false negatives. For a medical-risk project, recall and false-negative behavior are especially important, but no metric here makes the model clinically valid.

The `progress_log.csv` file records several model iterations, but the repo does not include a complete reproducibility package with dataset snapshot, split manifest, environment lockfile, random seeds, and generated evaluation artifacts.

## Limitations

- No external clinical validation.
- Unknown demographic and acquisition-device bias.
- Sensitive to image quality and distribution shift.
- Not evaluated as a medical device.
- No privacy or security controls around uploaded images.
- Raw model score is not calibrated as medical confidence.
- Dataset subset, split provenance, and license details need tighter documentation before broad public reuse.

## Required Disclaimer

This model is for educational and research purposes only. It is not FDA-approved, HIPAA-compliant, or clinically validated. Users should consult qualified medical professionals for health concerns.
