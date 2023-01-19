import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print("Error Occured!", e)
    else:
        print("success!")