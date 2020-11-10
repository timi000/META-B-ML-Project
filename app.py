from math import expm1

import joblib
from numpy.lib.twodim_base import diag
import pandas as pd
from flask import Flask, jsonify, request, render_template
#from tensorflow import keras
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('Diabetes_svm.pkl', 'rb'))



@app.route("/")
def index():

   return render_template ("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    #petName = float(request.form.get("petName"))
    #petAge=float(request.form.get("petLat"))
    #data=[petName, petAge]
    int_features = [float(x) for x in request.form.values()]
   
    print(int_features)
    x=[np.array(int_features)]
    print(x)
   
    prediction= model.predict(x)
    
    #prediction= np.argmax(model.predict(np.expand_dims(x, axis =0)), axis=-1)

    #pred =np.array2string(prediction, formatter={'float_kind':lambda x: "%.2f" % x})
    diab_pred = round(prediction[0],2)

    if diab_pred == 0:
        diab_pred = " The patience has high risk for Diabetes"

    else:
        diab_pred="The patience has low risk of Diabetes"




    print(diab_pred)
    return render_template("index.html", results=diab_pred)


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)




if __name__ == "__main__":
   
    app.run(debug=True)
