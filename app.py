from flask import Flask, request, jsonify, render_template
import joblib
import json
import numpy as np
import base64
import cv2
from wavelet import w2d

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    load_saved_artifacts()
    app.run(debug=True)


    
    

