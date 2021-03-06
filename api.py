# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:36:48 2019

@author: hp
"""




from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from flask import request
from datetime import datetime
import sys


# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    #print(request)
    if regressor:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            
            prediction = list(regressor.predict(query).astype("int64"))
            #print(prediction)
            
                
            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    regressor = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port)