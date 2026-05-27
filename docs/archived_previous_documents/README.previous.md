# Melanoma Model

Educational melanoma image-classification prototype built for EECS 582, Computer Science Capstone, Spring 2025.

This repository packages a Flask web interface, a TensorFlow/Keras binary image classifier, model-tracking artifacts, and documentation for architecture, limitations, governance, and security considerations.

## Portfolio Context

This was a collaborative capstone project. I served as a team lead responsible for coordinating project artifacts, tracking deadline readiness, and communicating with our supervisor to keep deliverables aligned with course and project expectations.

This repository is included on my GitHub as portfolio evidence of team leadership, project coordination, documentation discipline, and model-risk awareness. It should not be read as a claim of sole ownership over the full model, backend, or interface implementation.

## Important Disclaimer

This project is for educational and research purposes only.

It is not a medical device, not clinically validated, not FDA-approved, and not HIPAA-compliant. Do not use this project for diagnosis, treatment decisions, triage, patient-facing recommendations, or private medical-image handling. If you have a health concern, consult a qualified medical professional.

## What This Project Demonstrates

- Coordinating a machine-learning capstone across code, model, documentation, and deadline artifacts.
- Building a Flask upload interface around a TensorFlow/Keras image-classification model.
- Training and packaging a CNN-based melanoma classification prototype.
- Documenting preprocessing decisions, architecture, model limitations, and medical-risk disclaimers.
- Tracking model parameters and evaluation metrics across iterations.
- Identifying security, privacy, and deployment limitations before any production use.

## Repository Structure

| Path | Purpose |
|---|---|
| `backend/` | Flask app, templates, upload route, image preprocessing helper, and packaged Keras model. |
| `backend/templates/` | Prototype web pages for upload, education, about, contact, and disclaimer content. |
| `backend/requirements.txt` | Python dependencies for running the Flask prototype. |
| `model/` | Training and evaluation scripts, model parameters, and progress log. |
| `docs/` | Architecture, model card, development notes, governance, and project tracking documentation. |
| `SECURITY.md` | Security and privacy limitations for the prototype. |
| `LICENSE` | MIT license inherited from the project. |

## Quick Start

The web app expects `backend/melanoma_detector.keras` to exist.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

The app accepts `png`, `jpg`, and `jpeg` uploads, saves them to `backend/uploads/`, normalizes each image to `256x256`, and returns a JSON prediction response from the model.

## Model Workflow

Training and evaluation scripts live in `model/`.

```bash
cd model
python make_model.py
python test_model.py
```

These scripts expect a local dataset directory named `melanoma_cancer_dataset/` with `train/`, `validation/`, and `test/` splits containing `benign/` and `malignant/` class folders.

The dataset itself is not included in this repository.

## Documentation

- [Documentation Index](docs/README.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Model Card](docs/MODEL_CARD.md)
- [Project Governance](docs/PROJECT_GOVERNANCE.md)
- [Model Tracker](docs/melanoma_model_tracker.md)
- [TensorFlow Tools Guide](docs/tensorflow_tools_guide.md)
- [Security and Privacy](SECURITY.md)

## Current Limitations

- The prototype stores uploaded files locally and does not implement privacy controls.
- The model has not been clinically validated or externally audited.
- Runtime, training, and tracker thresholds are not fully unified across files.
- The repository currently includes sample uploaded images and a packaged model artifact.
- The app is not production hardened and should not be deployed for real health data.

## Dataset Acknowledgement

The project acknowledges the International Skin Imaging Collaboration (ISIC) as the dataset source.

Dataset source: [ISIC Archive](https://www.isic-archive.com/)

## Acknowledgements

Some preprocessing and normalization notes are adapted from the [TensorFlow image loading tutorial](https://www.tensorflow.org/tutorials/load_data/images).
