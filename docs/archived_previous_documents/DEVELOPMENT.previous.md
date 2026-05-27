# Development Guide

## Local App Setup

The Flask app lives in `backend/` and expects the packaged model artifact at `backend/melanoma_detector.keras`.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` after the server starts.

## Upload Behavior

The `/upload` route accepts files with these extensions:

- `png`
- `jpg`
- `jpeg`

Accepted files are saved to `backend/uploads/`. The app then:

1. Loads the saved image.
2. Resizes it to `256x256`.
3. Converts pixels from `[0, 255]` to `[0, 1]`.
4. Runs inference with `backend/melanoma_detector.keras`.
5. Converts the score into `Malignant` or `Benign`.
6. Returns JSON with `filename`, `prediction`, and `confidence`.

## Training Data Layout

The training and evaluation scripts expect a local dataset folder named `melanoma_cancer_dataset/` under `model/`.

```text
model/
  melanoma_cancer_dataset/
    train/
      benign/
      malignant/
    validation/
      benign/
      malignant/
    test/
      benign/
      malignant/
```

The dataset is not included in this repository.

## Training

From `model/`:

```bash
python make_model.py
```

The script reads `model_parameters.json`, trains a CNN with TensorFlow/Keras, evaluates on the test split, appends metrics to `progress_log.csv`, and saves `melanoma_detector.keras`.

## Evaluation

From `model/`:

```bash
python test_model.py
```

The script loads `melanoma_detector.keras`, predicts against the test split, prints a classification report, and displays a confusion matrix.

## Threshold Notes

Current threshold references are not fully aligned:

| Location | Threshold |
|---|---:|
| `backend/app.py` | `0.4` |
| `model/model_parameters.json` | `0.35` |
| `model/test_model.py` | `0.5` |
| `docs/melanoma_model_tracker.md` historical note | `0.7` |

Before presenting final model behavior, align these values or document why each context uses a different threshold.

## Repository Hygiene

Avoid committing:

- local virtual environments
- Python caches
- `.DS_Store`
- raw datasets
- private uploads
- generated plots
- ad hoc test images

The existing repository includes a model artifact and sample uploads because they were part of the capstone prototype state. Future cleanup should review whether those assets are licensed, necessary, and safe to keep public.

