# Decision Rationale

This document explains the major technical and organizational decisions in the current DermaScan prototype. The goal is to make the project easier to reproduce, evaluate, and improve as a takeover asset.

## Flask For The Web App

Flask was a good fit for the original prototype because it is lightweight, easy to understand, and fast to wire into a simple upload-and-predict workflow.

Why it made sense:

- Minimal setup for a student capstone and early proof of concept.
- Straightforward route definitions for pages like home, about, education, contact, and disclaimer.
- Easy file-upload handling through `request.files`.
- Simple JSON response path for returning model predictions to the browser.
- Works well for local demos without requiring a larger application framework.

Tradeoffs:

- Flask does not provide production structure by default.
- Security, authentication, rate limiting, validation, and observability must be added deliberately.
- A future commercial product may need a more structured API layer or service architecture.

Takeover recommendation:

Keep Flask for local demonstration and technical diligence. Reassess the web stack before any production or clinical pilot.

## TensorFlow/Keras For Modeling

TensorFlow/Keras was appropriate because the project needed a familiar image-classification framework with a simple path from training to saved model artifact.

Why it made sense:

- Keras Sequential models are approachable for CNN experimentation.
- The `.keras` model format packages architecture and weights for reuse.
- TensorFlow has built-in utilities for loading image datasets from directory structures.
- The ecosystem has strong documentation and broad educational support.

Tradeoffs:

- The current custom CNN is a baseline, not necessarily the strongest modern approach.
- Reproducibility requires stronger environment pinning, dataset manifests, and seed control.
- Future work should compare this baseline against transfer-learning models and modern vision architectures.

Takeover recommendation:

Preserve the current Keras model as a historical baseline. Build the next model iteration with reproducible experiment tracking and stronger evaluation discipline.

## CNN Baseline Architecture

The model uses a conventional convolutional neural network with convolution, pooling, batch normalization, dropout, dense layers, and sigmoid output.

Why it made sense:

- CNNs are a standard starting point for image classification.
- The architecture is understandable and explainable to a capstone audience.
- Binary sigmoid output matches the benign/malignant classification framing.
- Dropout and batch normalization show awareness of overfitting and training stability.

Tradeoffs:

- A hand-built CNN may underperform pretrained medical or general vision backbones.
- The model is not externally validated.
- The raw output score is not calibrated medical confidence.

Takeover recommendation:

Use this architecture as a baseline for comparison, not as the assumed final model.

## Directory-Based Dataset Loading

The training scripts expect images in `train/`, `validation/`, and `test/` folders with `benign/` and `malignant/` subfolders.

Why it made sense:

- TensorFlow can infer labels directly from folder names.
- The layout is easy for students and reviewers to understand.
- It keeps early training code compact.

Tradeoffs:

- Folder structure alone does not record dataset provenance.
- Reproducibility requires split manifests and source metadata.
- It is easy to accidentally change a split by moving files.

Takeover recommendation:

Keep the folder layout for local compatibility, but add dataset manifests before any serious evaluation.

## Local File Upload Storage

The prototype saves uploaded images to local disk.

Why it made sense:

- Simple to implement.
- Easy to debug during local demos.
- Avoided infrastructure work during the capstone phase.

Tradeoffs:

- Not safe for private or medical images.
- No retention policy.
- No encryption, isolation, or access control.
- Uploaded files previously became mixed with source-controlled project files.

Takeover recommendation:

Use `var/uploads/` only for local development. A future product should use secure temporary object storage, deletion policies, and explicit consent.

## Separate `dermascan_app`, `ml_pipeline`, `artifacts`, `data`, And `var`

The cleanup separates runtime app code, ML pipeline code, binary artifacts, local datasets, and runtime state.

Why it made sense:

- `dermascan_app/` clearly holds the web application.
- `ml_pipeline/` makes training, evaluation, config, and registry files easier to reproduce.
- `artifacts/` separates model binaries and sample inputs from source code.
- `data/` creates a predictable home for local datasets without committing them.
- `var/` separates runtime-generated files from project assets.

Tradeoffs:

- Existing paths had to be updated.
- Git shows many moves because the old layout was less intentional.

Takeover recommendation:

Keep this structure. It is more readable for future maintainers, investors, reviewers, and technical diligence.

## Archived Previous Documents

Previous documents were moved to `docs/archived_previous_documents/`.

Why it made sense:

- Preserves capstone history.
- Prevents old notes from competing with the active professional documentation.
- Allows reviewers to understand how the project matured.

Tradeoffs:

- Some duplicated historical claims remain in the archive.
- Readers must understand that archived files are not active operating docs.

Takeover recommendation:

Keep the archive, but treat the current docs as the source of truth.

## Conservative Medical Claims

The documentation avoids claims that the system diagnoses melanoma or is clinically ready.

Why it made sense:

- The project lacks clinical validation.
- The dataset provenance and evaluation package are incomplete.
- Medical AI claims create regulatory, ethical, and safety obligations.

Tradeoffs:

- The commercial story becomes more cautious.
- Marketing language is less flashy.

Takeover recommendation:

Stay disciplined. The strongest commercialization narrative is not hype; it is a credible path from prototype to governed decision-support asset.

