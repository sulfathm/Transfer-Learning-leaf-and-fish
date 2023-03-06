# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:39:41 2023

@author: user pc
"""

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/predict',methods=['POST'])
def home():
    print('hello world')
    return render_template("index2.html")
    
if __name__ == '__main__':
          
    app.run(port=8000)