from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import cv2
# import numpy as np
import util

app = Flask(__name__)

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    jaundice = request.form['jaundice']
    fatigue = request.form['fatigue']
    discomfort = request.form['discomfort']
    appetite = request.form['appetite']
    urine = request.form['urine']
    itchy_skin = request.form['itchySkin']
    bruising = request.form['bruising']
    nausea_vomiting = request.form['nauseaVomiting']
    smoking_status = request.form['smokingStatus']
    alcohol_consumption = request.form['alcoholConsumption']

    predicted_disease = util.predict_disease(jaundice, fatigue, discomfort, appetite, urine, itchy_skin, bruising, nausea_vomiting, smoking_status, alcohol_consumption)

    response = jsonify({
        'estimated_disease': predicted_disease
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route('/predict_image_disease', methods=['POST'])
# def predict_image_disease():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#     if file:
#         filename = secure_filename(file.filename)
#         # Save the uploaded file to a folder
#         file.save(filename)
#         # Read the saved image
#         # image = cv2.imread(filename)
#         # Call the function from util to predict using CNN model
#         # predicted_result = util.predict_image_disease(image)
#         return jsonify({'predicted_result': predicted_result})

if __name__ == "__main__":
    print("Starting Python Flask server for Disease Prediction...")
    util.load_saved_models()
    app.run()
