from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from PIL import Image
import pytesseract
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (CORS to connect backend to frontend)


@app.route('/')
def index():
    print("Index route accessed")
    return jsonify({"message": "Welcome to the Receipt Personal Expenses Tracker API"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    # Convert the uploaded file to an image
    image = Image.open(io.BytesIO(file.read()))
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    # Return the extracted text
    return jsonify({"message": "File received", "filename": file.filename, "extracted_text": text})

if __name__ == "__main__":
    app.run(debug=True)