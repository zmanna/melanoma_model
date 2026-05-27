# Technical Due Diligence

## Executive Summary

DermaScan is a working academic prototype with a complete but minimal path from image upload to model prediction. It has enough technical substance to justify further evaluation, but it is not ready for production, clinical use, or commercial deployment.

The strongest asset is the end-to-end shape: Flask app, Keras model, preprocessing helper, training script, evaluation script, and model progress log. The biggest gaps are reproducibility, dataset provenance, threshold consistency, repository hygiene, security, and clinical validation.

## What Exists

| Component | Evidence |
|---|---|
| Web app | `dermascan_app/app.py` provides routes and `/upload`. |
| UI templates | `dermascan_app/templates/` includes home, about, contact, disclaimer, and education pages. |
| Inference helper | `dermascan_app/inference.py` loads the model and preprocesses images. |
| Model artifact | `artifacts/models/current/melanoma_detector.keras`, Keras 3.8 format, saved April 27, 2025. |
| Training script | `ml_pipeline/training/train_cnn.py` builds, trains, evaluates, logs, and saves a CNN. |
| Evaluation script | `ml_pipeline/evaluation/evaluate_cnn.py` loads a saved model and prints metrics. |
| Parameters | `ml_pipeline/config/model_parameters.json` captures model configuration. |
| Tracking | `ml_pipeline/registry/progress_log.csv` records several metric rows. |

## Model Snapshot

The packaged model is a Keras Sequential CNN with:

- input shape `256x256x3`
- convolution filters increasing from 32 to 256
- max pooling blocks
- batch normalization in later convolution blocks
- flatten layer
- dense layer with 128 units
- dropout rate `0.35`
- final sigmoid output

This is a conventional early CNN approach for binary image classification. It is reasonable for a capstone prototype, but a serious product effort should compare it against modern transfer-learning and foundation-model approaches.

## Inference Behavior

The Flask app:

1. receives an uploaded file
2. validates the extension
3. saves the file to `var/uploads/`
4. checks that OpenCV can read it
5. loads `artifacts/models/current/melanoma_detector.keras`
6. resizes the image to `256x256`
7. scales pixels to `[0, 1]`
8. runs prediction
9. returns a label and raw model score

The UI calls the raw model score "confidence." That should be renamed or calibrated before any serious product use.

## Known Technical Gaps

| Gap | Why It Matters |
|---|---|
| Dataset not included | Training cannot be reproduced from the repo alone. |
| Dataset subset not fully specified | Results cannot be audited or compared reliably. |
| Thresholds differ across files | Runtime and evaluation behavior are not aligned. |
| No environment lockfile | Dependency versions may drift. |
| Training script is path-dependent | Scripts assume a specific working directory. |
| Metrics log has weak versioning | Logged rows use `version` as a literal value. |
| Uploaded images are committed | Raises hygiene, privacy, and licensing concerns. |
| No automated tests | Regressions are hard to catch. |
| No model calibration | Score should not be treated as clinical confidence. |

## Threshold Inventory

| Location | Threshold |
|---|---:|
| `dermascan_app/app.py` | `0.4` |
| `ml_pipeline/config/model_parameters.json` | `0.35` |
| `ml_pipeline/evaluation/evaluate_cnn.py` | reads `0.35` from config |
| archived tracker note | `0.7` |

The next technical owner should define one evaluation threshold policy and document any separate operating thresholds.

## Repository Hygiene Findings

The repository includes:

- `.DS_Store` files
- Python bytecode caches
- uploaded test images
- non-medical image uploads
- a large packaged model artifact

This is normal for a student prototype, but not acceptable for a professional public repository without cleanup and rationale.

## Diligence Verdict

DermaScan should be treated as an early technical asset, not a ready product.

Proceed if the goal is to:

- build a polished portfolio case study
- demonstrate AI product diligence
- explore dermatology AI workflows
- create a professional proof-of-concept plan

Do not proceed directly to:

- public medical deployment
- diagnosis claims
- patient data handling
- paid clinical pilots
- regulated product marketing
