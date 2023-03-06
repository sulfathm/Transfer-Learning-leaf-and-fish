# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:53:37 2023

@author: user pc
"""

from flask import Flask, request
from flask import Flask , request , render_template
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']  # assuming the file input field is named 'file'
    filename = file.filename
    print('Uploaded file:', filename)
    # do something with the uploaded file
    return 'File uploaded successfully'

@app.route('/')
def index():
    return render_template('index.html')
    
    #print(image_file)


if __name__ == '__main__':
          
    app.run()