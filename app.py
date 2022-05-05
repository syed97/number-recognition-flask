from urllib import response
from flask import Flask, request, render_template, jsonify
import os
import json
import base64
import numpy as np
import cv2
import re
import io
import matplotlib.pyplot as plt
from PIL import Image
from model_prod import predict_digit
from utility import *


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        response = jsonify({'data': 'post'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if request.method == 'GET':
        response = jsonify({'data': 'get'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/img', methods=['POST'])
def get_image():
    if request.method == "POST":
        r = request.form['imageBase64']
        img_data = base64.b64decode(r.split(",")[1]) # byte data for image
        img = transform_raw_image(img_data)
        prediction_data = predict_digit(img)
        print("Prediction is: ")
        print(prediction_data["predicted_value"])
        print("Prediction accuracy is: ")
        print(prediction_data["predicton_accuracy"])
        print("--------------------end----------------------")
        response = jsonify({
            'predicted_value': prediction_data["predicted_value"],
            'prediction_accuracy' : prediction_data["predicton_accuracy"]
        })
        print(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        print("no data recvd")


if __name__ == '__main__':
    app.run(debug=True) #, host='0.0.0.0')



# test code
        # image = Image.open(io.BytesIO(imgdata))
        # global count
        # count = count + 1
        # image.save('here_{}.png'.format(count))
        # image_np = np.array(image)
        # print(image_np)
        # img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)