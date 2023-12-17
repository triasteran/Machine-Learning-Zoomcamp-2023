import pickle

from flask import Flask
from flask import request
from flask import jsonify


import tensorflow as tf
from tensorflow import keras
from PIL import Image
from io import BytesIO
import requests

import numpy as np


model_file = 'cnn_v1_03_0.834.h5'

model = keras.models.load_model(model_file) 


app = Flask('gene_expression')

@app.route('/predict', methods=['POST'])
def predict():

    # get an input as path to image 
    sample_path = request.get_json()['img_path']
    
    response = requests.get(sample_path)   
    img = Image.open(BytesIO(response.content)).resize((150, 150),Image.NEAREST)

    # open it 
    #with Image.open(sample_path) as img:
    #    img = img.resize((150, 150), Image.NEAREST)

    # preprocess it 
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = X/ 255

    # now use the model to predict a class 
    pred = model.predict(X)[0]

    res = {'hem': str(pred[0]), 'all':str(1-pred[0])}

    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)