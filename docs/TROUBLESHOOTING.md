# Troubleshooting

## Flask App Does Not Start

Check that dependencies are installed:

```bash
cd dermascan_app
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

If TensorFlow import fails, confirm that your Python version and platform are compatible with the TensorFlow package being installed.

## Model File Not Found

The app expects:

```text
artifacts/models/current/melanoma_detector.keras
```

If this file is missing, restore the packaged model artifact or run training after preparing the dataset.

## Upload Returns "Invalid File Type"

The app currently accepts only:

- `png`
- `jpg`
- `jpeg`

File extension checking is not a complete security control. It is only a basic prototype filter.

## Upload Returns "Could Not Process The Image"

The file was saved, but OpenCV could not read it as an image.

Try:

- using a standard RGB JPEG or PNG
- checking that the file is not corrupted
- avoiding screenshots or non-image files renamed with image extensions

## Training Fails Because Dataset Directory Is Missing

Training expects:

```text
data/melanoma_cancer_dataset/
  train/
  validation/
  test/
```

Each split must contain `benign/` and `malignant/` folders.

## Evaluation Fails Because Test Data Is Missing

Evaluation expects:

```text
data/melanoma_cancer_dataset/test/benign/
data/melanoma_cancer_dataset/test/malignant/
```

The repository does not include the dataset.

## TensorFlow Or Keras Version Problems

The packaged model metadata reports Keras `3.8.0`. If loading fails:

- check the installed TensorFlow/Keras version
- install a compatible TensorFlow release
- regenerate the model artifact locally from the training script

TODO: Add pinned environment file after dependency versions are finalized.

## Results Differ Between Runs

The current training script does not set random seeds. Differences can occur from:

- random initialization
- dataset shuffling
- hardware/backend differences
- dependency version differences

For reproducible experiments, add explicit seed control and pinned dependencies.

## Runtime Prediction Differs From Evaluation Threshold

The Flask app currently uses a runtime threshold of `0.4`. The evaluation pipeline reads `0.35` from `ml_pipeline/config/model_parameters.json`.

This mismatch is documented as a technical gap. Align thresholds before comparing app behavior to evaluation metrics.

