from http.client import OK
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS

from utils import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():     
      
    data = request.files["myFile"]
    data.save(data.filename)
    result = predict_the_pic(data.filename)
    print(result)
    return jsonify({"Result" : "Done"})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
