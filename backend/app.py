from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    # Process the file (e.g., OCR) here
    # Placeholder response
    return jsonify({"message": "File received", "filename": file.filename})

if __name__ == "__main__":
    app.run(debug=True)