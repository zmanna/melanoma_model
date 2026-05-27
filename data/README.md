# Data Directory

This directory is reserved for local datasets and reproducibility manifests.

The melanoma image dataset is intentionally not committed. Training scripts expect the following local layout:

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

Before any commercial or clinical work, add dataset documentation that records:

- source
- license
- download date
- filtering criteria
- split manifest
- permitted use
- known demographic and image-acquisition limitations

