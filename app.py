from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')  # Serves your frontend page

@app.route('/remove-text', methods=['POST'])
def remove_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    filename = secure_filename(str(uuid.uuid4()) + '_' + image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)

    # Simulate "text removal" – in real app, call Replicate/AI API here
    # For now, we just return the uploaded image as output
    return jsonify({'success': True, 'image_url': f'/{image_path}'})
