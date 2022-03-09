from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
import os
import numpy as np

app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/saveImage", methods=['POST'])
def predict():
      #data = request.form.get['myFile']
     # arr = np.array(data)
     # print(arr)
      
      data = request.files["myFile"]
      data.save("pppnggg.png")
      return jsonify({"Result" : "Good"})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
