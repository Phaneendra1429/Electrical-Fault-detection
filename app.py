# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:28:18 2022

@author: new
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('LR.pkl', 'rb'))
@app.route('/')
def home():
    return "<center><h1>Electrical Fault detection </h1> </center>"

standard_to = StandardScaler()
@app.route("/predict", methods=['GET','POST'])
def predict():
    
    if request.method== 'POST':
        
        input_features =[float(x) for x in request.form.values()]
        Ia=input_features[0]
        Ib=input_features[1]
        Ic=input_features[2]
        Va=input_features[3]
        Vb=input_features[4]
        Vc=input_features[5]
        value=[[Ia,Ib,Ic,Va,Vb,Vc]]
        
        
        predection= model.predict(value)
        
        return render_template('index.html',prediction_text='Predicted Electrical Fault Detection {} '.format(predection))
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
