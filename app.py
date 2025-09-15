from flask import Flask, request, send_from_directory, jsonify
import os
import cv2
import secrets  # For generating secure random UID

app = Flask(__name__, static_url_path='', static_folder='public')

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image_file = request.files['image']
    if image_file.filename == '':
        return "No selected file", 400

    # Generate a 16-digit UID (number as string)
    uid = ''.join([str(secrets.randbelow(10)) for _ in range(16)])

    # Filenames with 16-digit UID
    original_filename = f'entracloud_{uid}_original.jpg'
    grayscale_filename = f'entracloud_{uid}_grayscale.jpg'

    original_path = os.path.join(UPLOAD_FOLDER, original_filename)
    grayscale_path = os.path.join(UPLOAD_FOLDER, grayscale_filename)

    # Save uploaded image
    image_file.save(original_path)

    # Read and convert to grayscale
    img_color = cv2.imread(original_path)
    gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(grayscale_path, gray)

    return jsonify({
        "original": f"/uploads/{original_filename}",
        "grayscale": f"/uploads/{grayscale_filename}"
    })


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/assets/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('assets/css', filename)


if __name__ == '__main__':
    app.run(debug=True)
