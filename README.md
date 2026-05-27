# DermaScan

Melanoma image classification prototype built with Flask and TensorFlow/Keras.

DermaScan is a Flask and TensorFlow/Keras prototype for binary skin-lesion image classification, organized as a reproducible scientific software asset for technical review, extension, and future validation.

## Overview

This repository contains an end-to-end educational prototype for classifying skin-lesion images as `benign` or `malignant`. It includes a local web application, an inference helper, a packaged Keras model artifact, training and evaluation scripts, model-configuration metadata, a historical progress log, and a professional documentation set.

The project began as an EECS 582 Computer Science Capstone project in Spring 2025. This repository has since been reorganized as if a serious technical team were taking over the prototype for further diligence. The current state is suitable for portfolio review, scientific-method discussion, and software-maintenance evaluation. It is not suitable for clinical deployment.

## Problem Statement

Early melanoma detection is clinically important, but automated skin-lesion classification is a high-risk medical AI problem. A useful computational prototype must do more than produce a label: it must make data assumptions, preprocessing, model behavior, validation gaps, and safety limitations explicit.

DermaScan addresses the technical prototype question:

> Can a small end-to-end system connect image upload, preprocessing, CNN inference, training scripts, evaluation scripts, and model-risk documentation in a way that future contributors can inspect and extend?

It does not answer the clinical question of whether the model is safe or effective for diagnosis.

## Motivation

This project is useful as a compact case study in:

- web-based ML inference with Flask
- image preprocessing for CNN classifiers
- TensorFlow/Keras model packaging
- binary classification evaluation
- model governance for health-adjacent AI
- documentation and reproducibility practices for scientific software

The strongest value of the repository is its complete prototype shape: app, model, training pipeline, evaluation path, artifacts, and documentation are all present and intentionally separated.

## Current Status

| Area | Status |
|---|---|
| Project type | Academic/scientific prototype |
| Interface | Flask web application |
| ML framework | TensorFlow/Keras |
| Model family | Convolutional neural network |
| Task | Binary image classification |
| Classes | `benign`, `malignant` |
| Input shape | RGB image resized to `256x256` |
| Output | Raw sigmoid-style score and thresholded label |
| Dataset | ISIC-acknowledged source; exact subset requires documentation |
| Packaged model | Included at `artifacts/models/current/melanoma_detector.keras` |
| Clinical validation | Not performed |
| Production readiness | Not ready |

## Critical Medical Disclaimer

This project is for educational, research, and technical-evaluation purposes only.

It is not a medical device, not FDA-approved, not HIPAA-compliant, not clinically validated, and not appropriate for diagnosis, treatment decisions, triage, reassurance, or patient-facing medical recommendations. Do not upload private medical images or protected health information. Consult a qualified medical professional for health concerns.

## Key Features

- Local Flask app with upload, preview, prediction, education, contact, and disclaimer pages.
- TensorFlow/Keras inference path using a packaged `.keras` model artifact.
- Training script for a configurable CNN baseline.
- Evaluation script using classification report and confusion matrix.
- Centralized model parameters in JSON.
- Historical model progress log in CSV format.
- Reorganized project structure for app code, ML pipeline code, artifacts, local data, runtime state, and documentation.
- Mermaid diagrams and scientific-method documentation.
- Explicit documentation of limitations, assumptions, and reproducibility gaps.

## Scientific And Technical Background

The current model is a conventional convolutional neural network for binary image classification. CNNs are commonly used for image tasks because convolutional filters can learn local spatial features such as edges, textures, shapes, and higher-order visual patterns.

The prototype uses:

- `Conv2D` layers for feature extraction
- `MaxPooling2D` layers for spatial downsampling
- `BatchNormalization` layers in later convolution blocks
- `Dropout` for regularization
- a dense hidden layer for classification
- a sigmoid output unit for binary classification

Images are resized to `256x256`, converted to arrays, and normalized from `[0, 255]` to `[0, 1]`.

## Repository Structure

```text
.
├── dermascan_app/                 # Flask runtime application
│   ├── app.py                     # Routes, upload handling, prediction endpoint
│   ├── inference.py               # Model loading and image preprocessing
│   ├── requirements.txt           # Minimal runtime dependencies
│   └── templates/                 # HTML/CSS interface templates
├── ml_pipeline/                   # Training/evaluation/reproducibility surface
│   ├── config/
│   │   └── model_parameters.json  # Model and training configuration
│   ├── evaluation/
│   │   └── evaluate_cnn.py        # Test-set evaluation script
│   ├── registry/
│   │   └── progress_log.csv       # Historical metric log
│   └── training/
│       └── train_cnn.py           # CNN training script
├── artifacts/
│   ├── models/current/            # Packaged model artifact
│   └── sample_inputs/             # Legacy sample uploads for review
├── data/                          # Local dataset location; dataset not committed
├── docs/                          # Professional documentation set
├── var/uploads/                   # Local runtime uploads; ignored by Git
├── SECURITY.md
├── LICENSE
└── README.md
```

See [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) for the naming rationale.

## Architecture Overview

At runtime, the Flask app receives an image, stores it locally under `var/uploads/`, verifies that OpenCV can read it, sends the path to the inference helper, loads the Keras model if needed, preprocesses the image, and returns a JSON prediction.

```text
Browser
  -> Flask /upload route
  -> local upload storage
  -> image validation
  -> TensorFlow preprocessing
  -> Keras model inference
  -> JSON response
```

Detailed architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)  
Mermaid diagrams: [docs/UML.md](docs/UML.md)

## Data Pipeline And Workflow

### Training Workflow

1. Place image data under `data/melanoma_cancer_dataset/`.
2. Organize data into `train`, `validation`, and `test` splits.
3. Use `benign` and `malignant` subdirectories for labels.
4. Read model settings from `ml_pipeline/config/model_parameters.json`.
5. Train the CNN with `ml_pipeline/training/train_cnn.py`.
6. Save the current model artifact to `artifacts/models/current/melanoma_detector.keras`.
7. Append metric summaries to `ml_pipeline/registry/progress_log.csv`.

### Inference Workflow

1. Run the Flask app.
2. Upload a `png`, `jpg`, or `jpeg` image.
3. The app stores the image in `var/uploads/`.
4. The image is resized to `256x256` and normalized.
5. The Keras model returns a raw sigmoid-style score.
6. The app thresholds the score and returns a label.

## Installation

### Prerequisites

- Python 3.10 or newer recommended.
- A local environment capable of installing TensorFlow.
- Optional: a local dataset if you want to reproduce training or evaluation.

### Runtime Setup

```bash
cd dermascan_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

### Dependency Notes

The current dependency file is intentionally minimal:

```text
opencv-python
flask
tensorflow
```

TODO: Add a pinned environment file for reproducible scientific runs.

## Configuration

Model configuration is stored in [ml_pipeline/config/model_parameters.json](ml_pipeline/config/model_parameters.json).

Current values:

| Parameter | Value |
|---|---:|
| `version` | `0.1` |
| `convolutional_layers` | `4` |
| `dense_layers` | `1` |
| `dense_nodes` | `128` |
| `batch_size` | `32` |
| `dropout` | `0.35` |
| `epochs` | `10` |
| `threshold` | `0.35` |

Runtime note: the Flask app currently uses a runtime threshold of `0.4`, while the ML pipeline config uses `0.35`. This is documented as a technical gap and should be reconciled before any formal model release.

## Usage Examples

### Run The Local Web App

```bash
cd dermascan_app
source .venv/bin/activate
python app.py
```

### Train The CNN Baseline

```bash
python ml_pipeline/training/train_cnn.py
```

### Evaluate The Current Model

```bash
python ml_pipeline/evaluation/evaluate_cnn.py
```

## Input Requirements

### Web App

- Accepted extensions: `png`, `jpg`, `jpeg`
- Intended input: skin-lesion image
- Runtime storage: `var/uploads/`
- Prohibited input: private medical images, patient data, protected health information, or identifying photos

### Training And Evaluation

Expected local dataset layout:

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

TODO: Add exact dataset citation, version, download date, filtering criteria, and split manifest.

## Outputs And Results

### Web App Response

The `/upload` endpoint returns JSON:

```json
{
  "filename": "example.jpg",
  "prediction": "Benign",
  "confidence": 0.1234
}
```

The `confidence` field is a raw model score, not calibrated medical confidence.

### Training Outputs

- `artifacts/models/current/melanoma_detector.keras`
- appended row in `ml_pipeline/registry/progress_log.csv`
- printed TensorFlow training history
- displayed metric plots
- displayed confusion matrix

### Evaluation Outputs

- printed class labels
- printed classification report
- printed confusion matrix
- displayed confusion-matrix heatmap

## Methodology

The current pipeline:

1. Loads images from directory-labeled class folders.
2. Resizes each image to `256x256`.
3. Normalizes pixel values to `[0, 1]`.
4. Trains a CNN with convolutional, pooling, batch normalization, dense, dropout, and sigmoid layers.
5. Uses binary cross-entropy loss and Adam optimization.
6. Evaluates predictions with accuracy, precision, recall, F1 score, and confusion matrix.

Detailed methodology: [docs/METHODOLOGY.md](docs/METHODOLOGY.md)

## Model Details

The packaged model at `artifacts/models/current/melanoma_detector.keras` was saved with Keras `3.8.0` on `2025-04-27`.

Layer summary:

| Stage | Details |
|---|---|
| Input | `256x256x3` RGB image |
| Convolution blocks | Filters: `32`, `64`, `128`, `256`; kernel size `3x3` |
| Pooling | Max pooling after each convolution block |
| Normalization | Batch normalization after later convolution layers |
| Dense layer | `128` units, ReLU |
| Regularization | Dropout `0.35` |
| Output | Single sigmoid unit |

## Evaluation Metrics

The project tracks:

- accuracy
- precision
- recall
- F1 score
- confusion matrix

For this domain, false negatives are especially important because an incorrect benign label could create false reassurance. However, no metric currently establishes clinical validity.

## Results Summary

The historical progress log contains five recorded iterations. The best logged row reports:

| Metric | Value |
|---|---:|
| Accuracy | `0.893` |
| Recall | `0.9154` |
| Precision | `0.866` |
| F1 score | `0.8900` |

These values should be treated as historical prototype metrics only. They are not externally validated, not tied to a complete reproducibility package, and not sufficient for medical claims.

## Reproducibility

Current reproducibility status:

| Requirement | Status |
|---|---|
| Source code | Present |
| Packaged model artifact | Present |
| Training script | Present |
| Evaluation script | Present |
| Dataset | Not included |
| Dataset manifest | TODO |
| Environment lockfile | TODO |
| Random seeds | TODO |
| Generated benchmark artifacts | TODO |

Detailed instructions: [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md)

## Testing

There is currently no automated test suite.

Recommended tests:

- Flask route smoke tests
- upload validation tests
- preprocessing shape/range tests
- model artifact existence test
- evaluation script dry-run with a tiny fixture dataset
- documentation link checks

## Troubleshooting

Common issues are documented in [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).

## Limitations

- Dataset subset, provenance, and license terms are incomplete.
- Training cannot be fully reproduced without the local dataset.
- Model performance has not been externally validated.
- Runtime and evaluation thresholds are not fully unified.
- The raw sigmoid score is not calibrated confidence.
- The app does not implement production security or privacy controls.
- The current UI is not designed for clinical workflow.
- Historical sample uploads require privacy and licensing review before public promotion.

## Future Work

Near-term engineering:

- pin dependencies
- add automated tests
- align threshold policy
- rename `confidence` to `score` or calibrate the model
- add dataset manifests
- create reproducible evaluation reports

Scientific/modeling:

- compare against transfer-learning baselines
- perform calibration analysis
- evaluate subgroup and acquisition-device performance
- add external validation data
- document threshold-selection rationale

Product/governance:

- design clinician-in-the-loop workflows
- define security and privacy controls
- obtain regulatory and legal review before any clinical pilot

## Citation And Academic Use

If referencing this repository in academic or portfolio contexts, cite it as an educational prototype unless and until a formal publication or release artifact exists.

Suggested citation placeholder:

```text
Zutshi, A. and EECS 582 Team 33. DermaScan: Melanoma Image Classification Prototype.
Computer Science Capstone, Spring 2025. GitHub repository.
TODO: Add repository DOI or archival release URL.
```

TODO: Add complete team attribution, institutional affiliation, dataset citation, and permanent archive link if this project is prepared for publication.

## Contributing

Contributions should prioritize reproducibility, safety, and clear documentation.

Recommended contribution areas:

- dependency pinning
- tests
- dataset manifest tooling
- model evaluation reports
- safer upload handling
- documentation improvements
- model-card release templates

Before proposing changes that affect model behavior, document the dataset, threshold, metrics, and expected risk impact.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).

## Contact

TODO: Add maintainer contact, project owner, or preferred issue tracker.
