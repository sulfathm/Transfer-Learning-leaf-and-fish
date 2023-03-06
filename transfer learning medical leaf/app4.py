# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:34:33 2023

@author: user pc
"""

from flask import Flask , request , render_template
import tensorflow as tf
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pickle
import cv2

app=Flask(__name__)

#model = load_model('weights.h5')

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    file=(request.values['file'])
    path="static/test/"+file
    print(path)
    model = tf.keras.models.load_model('weights.h5')
    def testing_image(image_directory):
        # image = load_img(image_file, target_size=(224, 224))
        # image = img_to_array(image)
        # image = np.expand_dims(image, axis=0)
        # image = image / 255.0
        test_image = load_img(image_directory,target_size = (224,224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image , axis=0)
        test_image = test_image/255
        result = model.predict(x = test_image)
        print(result)

        if np.argmax(result)  == 0:        
            prediction = 'Arive-dantu'
        elif np.argmax(result)  == 1:
            prediction = 'Basale'
        elif np.argmax(result)  == 2:
            prediction = 'Jackfruite'
        elif np.argmax(result)  == 3:
            prediction = 'Neem'
        elif np.argmax(result)  == 4:
            prediction = 'Roxburg fig'
        elif np.argmax(result)  == 5:
            prediction = 'Sinesis'
        elif np.argmax(result)  == 6:
            prediction = 'jasmine'
        elif np.argmax(result)  == 7:
            prediction = 'Karanda'
        elif np.argmax(result)  == 8:
            prediction = 'mustard'
        else:
           prediction = 'peepal'
        return prediction
    
    x=(testing_image(path))
    print(x)
    return render_template('result.html',prediction_text=(x))
   
   
if __name__ == '__main__':
          
    app.run(port=8000)
    