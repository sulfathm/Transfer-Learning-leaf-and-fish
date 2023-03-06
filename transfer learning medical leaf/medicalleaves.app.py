# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:39:38 2023

@author: user pc
"""

from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
#model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    
    file=(request.values['file'])
    x="static/test/"+file
    print(x)

    #print("helloooooo")
    

    return render_template('index2.html')
if __name__ == '__main__':
          
    app.run(port=8000)