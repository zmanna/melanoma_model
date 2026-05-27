# Architecture

## Purpose

This project is an academic melanoma image-classification prototype built for EECS 582. It combines a TensorFlow/Keras model, a Flask web interface, image preprocessing, and documentation around model tracking and limitations.

## System Layout

```text
browser
  -> Flask app
  -> upload route
  -> saved image
  -> preprocessing helper
  -> Keras model
  -> JSON prediction response
```

## Runtime Components

| Path | Responsibility |
|---|---|
| `backend/app.py` | Flask app, page routes, upload endpoint, prediction response. |
| `backend/image_normal.py` | Model loading and image normalization/inference helper. |
| `backend/melanoma_detector.keras` | Packaged trained model artifact used by the web app. |
| `backend/templates/` | HTML/CSS pages for home, about, contact, education, and disclaimer. |
| `model/make_model.py` | CNN training script and metric logging. |
| `model/test_model.py` | Test-set evaluation script. |
| `model/model_parameters.json` | Training/version configuration. |
| `model/progress_log.csv` | Model iteration tracking artifact. |
| `docs/melanoma_model_tracker.md` | Model architecture, preprocessing, tracking, limitations, and risk notes. |
| `docs/tensorflow_tools_guide.md` | TensorFlow/preprocessing reference notes. |

## Inference Flow

1. User uploads an image through the Flask interface.
2. `backend/app.py` checks that the request contains a file and that its extension is allowed.
3. The filename is sanitized with `secure_filename` and written to `backend/uploads/`.
4. OpenCV checks that the saved file can be read as an image.
5. `backend/image_normal.py` lazily loads `backend/melanoma_detector.keras`.
6. The image is resized to `256x256`, converted to an array, normalized to `[0, 1]`, and passed to the model.
7. The app converts the model score into `Malignant` or `Benign`.
8. The route returns JSON containing filename, prediction label, and confidence score.

## Runtime Threshold

The current Flask route labels scores greater than `0.4` as `Malignant`; all other scores are labeled `Benign`.

That runtime threshold differs from other references in the repository:

| Location | Threshold |
|---|---:|
| `backend/app.py` | `0.4` |
| `model/model_parameters.json` | `0.35` |
| `model/test_model.py` | `0.5` |
| `docs/melanoma_model_tracker.md` historical note | `0.7` |

This should be reconciled before the project is presented as a stable model artifact.

## Training Flow

1. `model/model_parameters.json` defines version, image counts, architecture parameters, batch size, dropout, epochs, and threshold.
2. `model/make_model.py` loads train/validation/test directories through TensorFlow image dataset utilities.
3. Images are resized and normalized.
4. A CNN is built with convolution, pooling, batch normalization, dense, dropout, and sigmoid output layers.
5. Metrics are logged into `model/progress_log.csv`.
6. The model is saved as `melanoma_detector.keras`.

## Current Engineering Gaps

- Uploaded files are stored locally and are not protected as medical/private data.
- The app is not production hardened.
- There is no authentication, encryption, or retention policy.
- Model artifacts and uploaded images are committed to the repository.
- Runtime, evaluation, parameter, and tracker thresholds should be aligned.
- Training scripts assume a local dataset path that is not included in the repository.
- The app returns a score labeled as confidence, but the value is the raw sigmoid-style model output rather than a calibrated clinical confidence measure.
