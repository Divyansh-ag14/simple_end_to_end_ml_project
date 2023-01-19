import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)

model = pickle.load(open("regmodel.pkl", "rb"))
scalar = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json["data"]
    print("data", data)
    print("reshaped_data", np.array(list(data.values())).reshape(1,-1))
    scaled_data = scalar.fit_transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(scaled_data)
    print("output", output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print("Error Occured!", e)
    else:
        print("success!") 