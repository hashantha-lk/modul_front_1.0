from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import base64

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
MODIFIED_UPLOAD_FOLDER = 'modified_uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(MODIFIED_UPLOAD_FOLDER):
    os.makedirs(MODIFIED_UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODIFIED_UPLOAD_FOLDER'] = MODIFIED_UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return jsonify({'file_path': file_path})

@app.route('/save_modified', methods=['POST'])
def save_modified_image():
    data = request.json
    image_data = data['image_data']
    filename = data['filename']
    image_data = base64.b64decode(image_data.split(',')[1])
    file_path = os.path.join(app.config['MODIFIED_UPLOAD_FOLDER'], filename)
    with open(file_path, 'wb') as f:
        f.write(image_data)
    return jsonify({'file_path': file_path})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/modified_uploads/<filename>')
def modified_uploaded_file(filename):
    return send_from_directory(app.config['MODIFIED_UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)