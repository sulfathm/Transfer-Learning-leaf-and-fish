# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:30:14 2023

@author: user pc
"""

from flask import Flask , request , render_template
import tensorflow as tf
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pickle

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    return render_template('index.html')

# Define a route to display the form
#@app.route('/')
#def index():
    #return render_template('index.html')





if __name__ == '__main__':
          
    app.run(port=8000)