from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
model = None

@app.route('/predict', methods=['POST'])
def predict():
    global model
    try:
        if model is None:
            if not os.path.exists('model.pkl'):
                return jsonify({'error': 'Model file not found. Please train the model first.'}), 400
            model = joblib.load('model.pkl')

        payload = request.get_json()
        input_data = payload['input_data']
        features = np.array(input_data['data'])

        predictions = model.predict(features)
        probabilities = model.predict_proba(features)

        response = []
        for i in range(len(predictions)):
            response.append({
                'index': input_data['index'][i],
                'prediction': int(predictions[i]),
                'default_probability': float(probabilities[i][1])
            })

        return jsonify({'predictions': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
