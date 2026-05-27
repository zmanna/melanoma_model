# Methodology

This document describes the scientific and computational methodology used by the DermaScan prototype. It also identifies assumptions and missing metadata required for rigorous publication-quality use.

## Task Definition

DermaScan is framed as a binary image-classification prototype:

- input: RGB skin-lesion image
- output: model score and thresholded class label
- classes: `benign`, `malignant`

The current system should be interpreted as a technical demonstration, not a clinically validated diagnostic method.

## Dataset Assumptions

The repository acknowledges the International Skin Imaging Collaboration (ISIC) as the dataset source in archived project materials, but the active repository does not include a complete dataset manifest.

Known assumptions:

- Images are organized into class-labeled folders.
- Folder names provide labels.
- The expected labels are `benign` and `malignant`.
- Dataset splits are expected to exist before training.

Missing information:

- TODO: Add exact dataset name, subset, and version.
- TODO: Add dataset license and permitted-use terms.
- TODO: Add download date.
- TODO: Add filtering and exclusion criteria.
- TODO: Add train/validation/test split manifest.
- TODO: Add class counts for each split.
- TODO: Add demographic and image-acquisition metadata if available.

## Preprocessing

Both training and inference use the same core image normalization idea:

1. Load an image.
2. Resize to `256x256`.
3. Convert to an RGB-like tensor/array.
4. Scale pixel values from `[0, 255]` to `[0, 1]`.

The current implementation does not document color-space conversion assumptions beyond TensorFlow image loading. Future work should ensure that training and inference use one shared preprocessing function.

## Model Architecture

The current model is a Keras Sequential convolutional neural network.

| Stage | Description |
|---|---|
| Input | `256x256x3` image tensor |
| Convolution block 1 | `Conv2D(32, 3x3, relu)` then max pooling |
| Convolution blocks 2-4 | `Conv2D` filters `64`, `128`, `256`; batch normalization; ReLU activation; max pooling |
| Flatten | Converts feature maps to a dense vector |
| Dense | `128` ReLU units |
| Regularization | Dropout `0.35` |
| Output | Single sigmoid unit |

The architecture is suitable as an educational CNN baseline. It should not be assumed to be optimal for dermatology imaging.

## Training Procedure

Training is implemented in `ml_pipeline/training/train_cnn.py`.

The script:

1. Reads configuration from `ml_pipeline/config/model_parameters.json`.
2. Loads image splits from `data/melanoma_cancer_dataset/`.
3. Normalizes pixel values.
4. Builds the CNN architecture.
5. Compiles the model with Adam and binary cross-entropy.
6. Tracks accuracy, precision, and recall during training.
7. Trains for the configured number of epochs.
8. Saves the model to `artifacts/models/current/melanoma_detector.keras`.
9. Evaluates on the test split.
10. Appends summary metrics to `ml_pipeline/registry/progress_log.csv`.

## Evaluation Procedure

Evaluation is implemented in `ml_pipeline/evaluation/evaluate_cnn.py`.

The script:

1. Loads model configuration.
2. Loads the test split.
3. Normalizes image tensors.
4. Loads the packaged model artifact.
5. Generates sigmoid-style prediction scores.
6. Applies the configured threshold.
7. Prints a classification report.
8. Prints and displays a confusion matrix.

## Metrics

The project tracks:

| Metric | Meaning |
|---|---|
| Accuracy | Overall fraction of correct predictions. |
| Precision | Fraction of predicted malignant cases that are actually malignant. |
| Recall | Fraction of actual malignant cases predicted as malignant. |
| F1 score | Harmonic mean of precision and recall. |
| Confusion matrix | Counts of true negatives, false positives, false negatives, and true positives. |

For this problem domain, recall and false-negative analysis are especially important. A false benign result could create unsafe reassurance.

## Thresholding

The ML pipeline configuration uses `threshold = 0.35`. The Flask app currently uses `0.4` for runtime labeling.

This mismatch should be resolved before any formal model release. A future threshold policy should document:

- selected operating threshold
- validation dataset used
- sensitivity/recall tradeoff
- false-positive burden
- intended workflow and user population
- calibration status

## Scientific Assumptions

The current prototype assumes:

- directory labels are correct
- images are appropriate skin-lesion inputs
- train/validation/test splits are representative
- resizing to `256x256` preserves sufficient signal
- a binary benign/malignant label space is adequate for the prototype task

These assumptions require validation before scientific or clinical claims.

## Known Methodological Limitations

- No external validation set is documented.
- Dataset provenance is incomplete.
- No subgroup performance analysis is available.
- No image-acquisition-device analysis is available.
- No calibration analysis is available.
- No uncertainty quantification is implemented.
- No formal clinical workflow is defined.
- No model-card release record exists for the packaged artifact.

## Recommended Next Experiments

1. Rebuild the dataset with a documented split manifest.
2. Establish a reproducible baseline using the current CNN.
3. Compare against transfer-learning baselines.
4. Evaluate calibration and threshold sensitivity.
5. Report confusion matrices by relevant cohorts if metadata permits.
6. Create a model card for each trained artifact.
7. Preserve generated evaluation reports with the model release.

