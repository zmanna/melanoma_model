# Development Guide

## Local App

```bash
cd dermascan_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

Do not upload real patient images or private photos.

## Runtime Dependencies

The current dependency file is minimal:

```text
opencv-python
flask
tensorflow
```

A professional rebuild should pin versions and separate runtime, training, and development dependencies.

## Dataset Layout

Training scripts expect:

```text
data/melanoma_cancer_dataset/
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

The dataset is not committed. Any future dataset must include a license, source, download date, filtering criteria, split manifest, and permitted-use notes.

## Training

```bash
python ml_pipeline/training/train_cnn.py
```

The script reads `ml_pipeline/config/model_parameters.json`, builds a CNN, trains on the local dataset, evaluates on the test split, appends metrics to `ml_pipeline/registry/progress_log.csv`, and saves `artifacts/models/current/melanoma_detector.keras`.

## Evaluation

```bash
python ml_pipeline/evaluation/evaluate_cnn.py
```

The script loads `artifacts/models/current/melanoma_detector.keras`, predicts against the test split, prints a classification report, prints a confusion matrix, and displays a heatmap.

## Immediate Engineering Cleanup

Recommended first pass:

- remove tracked `.DS_Store` files
- remove tracked `__pycache__` files
- decide whether sample uploads belong in public history
- pin dependency versions
- create smoke tests for Flask routes
- move upload storage outside the repo
- align thresholds across training, evaluation, and runtime
- rename exposed `confidence` to `score` unless calibrated
- document model artifact provenance

## Commands Worth Adding Later

Future maintainers should consider a `Makefile` or task runner with:

```bash
make install
make run
make test
make train
make evaluate
make clean
```
