# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:01:46 2023

@author: user pc
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 1 11:01:46 2023
@author: user pc
"""

from flask import Flask, request, render_template
import tensorflow as tf
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pickle
import cv2

app = Flask(__name__)

# model = load_model('weights.h5')

@app.route('/')
def home():
    return render_template('fish.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = (request.values['file'])
    path = "static/test image/" + file
    print(path)

    model = tf.keras.models.load_model('weights model.h5')
    
    def testing_image(image_directory):
        test_image = load_img(image_directory, target_size=(224, 224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255
        result = model.predict(x=test_image)
        print(result)
        if np.argmax(result) == 0:
            prediction = 'Bangus'
        elif np.argmax(result) == 1:
            prediction = 'Catfish'
        elif np.argmax(result) == 2:
            prediction = 'Freshwater Eel'
        elif np.argmax(result) == 3:
            prediction = 'Goby'
        elif np.argmax(result) == 4:
            prediction = 'Gold Fish'
        elif np.argmax(result) == 5:
            prediction = 'Green spotted fish'
        elif np.argmax(result) == 6:
            prediction = 'jaguar gapote'
        elif np.argmax(result) == 7:
            prediction = "Silver Barb"
        elif np.argmax(result) == 8:
            prediction = "Snakehead"
        else:
            prediction = "Tilapia"
        return prediction

    x = testing_image(path)
    print(x)
    return render_template('fishresult.html', prediction_text=(x))


if __name__ == '__main__':
    app.run(port=8000)
