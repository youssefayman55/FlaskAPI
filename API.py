from flask import Flask, request, jsonify
import joblib
import os
import numpy as np

base_dir = 'C:/Users/S_AFRICA/Machine learning/Collage Project/Deyployment'
classifier_path = os.path.join(base_dir, 'classification_model.pkl')

try:
    model = joblib.load(classifier_path)
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    exit()

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def receive_data():
    data = request.json
    response = classify(data)
    return jsonify(response)

def classify(data):
    try:
        # Initialize a list to hold the classifications
        results = []
        for entry in data:
            # Fetch and convert input data
            hr = int(entry["Heart Rate"])
            age = int(entry["Age"])

            # Create a feature array
            features = np.array([[hr, age]])

            # Predict using the model
            classification = model.predict(features)

            # Append the result
            results.append({'Classification': classification.tolist()})


        return results

    except Exception as e:
        # Return a JSON with the error message
        return {'error': str(e)}, 400
    

