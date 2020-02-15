#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    l=[]
    l.append(request.form['value1'])
    l.append(request.form['value2'])
    l_final = np.array(l).reshape((1,-1))
    prediction = model.predict(l_final)
    final_Price = np.round(prediction.astype(int),-1)
    
    KM = request.form['value1']
    QTY = request.form['value2']
    str_KM = str(KM)
    str_QTY = str(QTY)
    final_note = "台七甲 "+str_KM+" 公里\n"+"載運 "+str_QTY+" 立方米\n"+" 每米含運費單價：\n"
    str_yuan = "元(未稅)"
    return render_template('index.html',prediction=final_Price,note=final_note,yuan=str_yuan)

if __name__ == "__main__":
    app.run(debug=True)

