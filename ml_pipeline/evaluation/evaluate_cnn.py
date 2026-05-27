"""Evaluate the current DermaScan model artifact on the local test split."""

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import json
from pathlib import Path

IMAGE_SIZE = (256, 256)
PIPELINE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PIPELINE_ROOT.parent
CONFIG_PATH = PIPELINE_ROOT / 'config' / 'model_parameters.json'
DATA_DIR = PROJECT_ROOT / 'data' / 'melanoma_cancer_dataset'
MODEL_PATH = PROJECT_ROOT / 'artifacts' / 'models' / 'current' / 'melanoma_detector.keras'

with open(CONFIG_PATH, 'r') as f:
    params = json.load(f)

test_dir = DATA_DIR / "test"
threshold = params["threshold"]
batch_size = params["batch_size"]

test = tf.keras.utils.image_dataset_from_directory(
    test_dir,
    label_mode='binary',
    image_size=IMAGE_SIZE,
    batch_size=batch_size,
    shuffle=False
)

class_names = test.class_names
print("Class Labels:", class_names)

test = test.map(lambda x,y: (x/255.0, y))

model = tf.keras.models.load_model(MODEL_PATH)

y_pred_prob = model.predict(test)

y_pred = (y_pred_prob > threshold).astype(int)

y_true = np.concatenate([y for x, y in test], axis=0)

print("\nClassification Report:\n", classification_report(y_true, y_pred, target_names=class_names))

conf_matrix = confusion_matrix(y_true, y_pred)
print(conf_matrix)
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
