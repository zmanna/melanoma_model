"""Inference utilities for the DermaScan Flask prototype."""

import numpy as np
import tensorflow as tf
from pathlib import Path

model = None
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / 'artifacts' / 'models' / 'current' / 'melanoma_detector.keras'
MODEL_INPUT_SIZE = (256, 256)

def load_model():
    """Load and cache the packaged Keras model artifact."""
    global model
    if model is None:
        model = tf.keras.models.load_model(MODEL_PATH)
    return model


def predict_lesion(image_path):
    """Return the raw sigmoid-style model score for one image path.

    Args:
        image_path: Filesystem path to an image readable by TensorFlow/Keras.

    Returns:
        A float-like scalar from the model's sigmoid output. This value is not
        calibrated medical confidence.
    """
    model = load_model()

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=MODEL_INPUT_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0
    
    img_tensor = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_tensor)[0][0]
    
    return prediction
