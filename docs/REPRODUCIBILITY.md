# Reproducibility

This document explains what can and cannot currently be reproduced from the repository.

## Reproducibility Status

| Asset | Status |
|---|---|
| Source code | Present |
| Packaged model artifact | Present |
| Training script | Present |
| Evaluation script | Present |
| Model configuration | Present |
| Historical progress log | Present |
| Dataset | Not included |
| Dataset manifest | TODO |
| Environment lockfile | TODO |
| Random seed strategy | TODO |
| Generated evaluation reports | TODO |

## Environment Setup

Create and activate a Python environment:

```bash
cd dermascan_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The current dependency file is minimal and unpinned. For strict reproducibility, future work should add a pinned `requirements-lock.txt`, `environment.yml`, or equivalent.

## Dataset Layout

Training and evaluation expect:

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

The dataset is intentionally not committed.

## Dataset Manifest Requirements

A publication- or review-ready dataset manifest should include:

- dataset name
- source URL or accession
- citation
- license
- download date
- preprocessing/filtering rules
- split generation method
- image IDs in each split
- class counts
- known demographic metadata
- known image-acquisition metadata

TODO: Add dataset manifest.

## Reproduce Local Inference

Run the app:

```bash
cd dermascan_app
source .venv/bin/activate
python app.py
```

Open `http://127.0.0.1:5000` and upload a non-private test image.

Expected behavior:

- upload is saved under `var/uploads/`
- model artifact is loaded from `artifacts/models/current/melanoma_detector.keras`
- JSON result includes `filename`, `prediction`, and `confidence`

## Reproduce Training

From the repository root:

```bash
python ml_pipeline/training/train_cnn.py
```

Requirements:

- dataset exists under `data/melanoma_cancer_dataset/`
- dependencies are installed
- local machine can run TensorFlow training

Outputs:

- updated `artifacts/models/current/melanoma_detector.keras`
- appended metrics in `ml_pipeline/registry/progress_log.csv`
- plots displayed interactively

## Reproduce Evaluation

From the repository root:

```bash
python ml_pipeline/evaluation/evaluate_cnn.py
```

Requirements:

- test split exists under `data/melanoma_cancer_dataset/test/`
- model artifact exists under `artifacts/models/current/`

Outputs:

- printed classification report
- printed confusion matrix
- displayed confusion-matrix heatmap

## Known Reproducibility Gaps

- Dataset is unavailable in the repository.
- Dataset split membership is not documented.
- Dependency versions are not pinned.
- Random seeds are not set.
- Hardware/runtime details are not recorded.
- Evaluation plots are displayed but not saved as versioned artifacts.
- Progress log version field historically contains the literal string `version`.

## Reproducible Release Checklist

Before tagging a scientific release:

- [ ] Pin dependencies.
- [ ] Add dataset citation and manifest.
- [ ] Record dataset split file IDs.
- [ ] Add random seed strategy.
- [ ] Save evaluation reports to disk.
- [ ] Save confusion matrix artifacts.
- [ ] Record model artifact checksum.
- [ ] Create a model card.
- [ ] Document threshold policy.
- [ ] Add automated tests.
- [ ] Archive release with a permanent DOI or release URL.

