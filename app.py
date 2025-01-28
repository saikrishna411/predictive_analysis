from flask import Flask, request, jsonify
from model import train_model, make_prediction, load_model
import os

app = Flask(__name__)
model = None  # Placeholder for the trained model

@app.route("/")
def home():
    return "Welcome to the Predictive Analysis API!"

@app.route('/upload', methods=['POST'])
def upload_data():
    # Check if 'file' is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided in the request"}), 400

    file = request.files['file']  # Get the file
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    # Save the uploaded file
    upload_path = os.path.join("data", "sample_data.csv")
    file.save(upload_path)
    
    return jsonify({"message": "File successfully uploaded"}), 200 

@app.route('/train', methods=['POST'])
def train():
    global model
    metrics = train_model('data/sample_data.csv')
    return jsonify(metrics), 200

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if not model:
        model = load_model()
    data = request.get_json()
    prediction = make_prediction(data, model)
    return jsonify(prediction), 200

if __name__ == '__main__':
    app.run(debug=True)
