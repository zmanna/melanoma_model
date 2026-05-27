"""Local Flask application for the DermaScan prototype.

The app provides simple informational pages and a `/upload` endpoint that
stores an image locally, validates that it can be decoded, sends it through
the inference helper, and returns a JSON prediction response.
"""

from flask import Flask, render_template, request, jsonify
import os
from pathlib import Path
from werkzeug.utils import secure_filename
import inference
import cv2

app = Flask(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPLOAD_FOLDER = PROJECT_ROOT / 'var' / 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
RUNTIME_MALIGNANT_THRESHOLD = 0.4
app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Return whether a filename uses an extension accepted by the prototype."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render the upload page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the project overview page."""
    return render_template('about.html')

@app.route('/education')
def education():
    """Render educational skin-lesion information."""
    return render_template('education.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/disclaimer')
def disclaimer():
    """Render the medical disclaimer page."""
    return render_template('disclaimer.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle an uploaded image and return the model's prototype prediction.

    The returned `confidence` value is the raw sigmoid-style model score. It is
    not calibrated clinical confidence and should not be interpreted as medical
    probability.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    file.save(filepath)
    
    image = cv2.imread(filepath)
    
    if image is None:
        return jsonify({'error': 'Could not process the image'}), 400
        
    prediction = inference.predict_lesion(filepath)
    print("PREDICTION", prediction)
    
    prediction_result = None
    if prediction > RUNTIME_MALIGNANT_THRESHOLD:
        prediction_result = 'Malignant'
    else:
        prediction_result = 'Benign'
    
    return jsonify({'filename': filename, 'prediction': prediction_result, 'confidence': float(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
