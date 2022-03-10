from http.client import OK
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS

from utils import *


app = Flask(__name__)
CORS(app)

__model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():     
   try:   
    data = request.files["myFile"]
    data.save(data.filename)
    result = predict_the_pic(data.filename,model=__model)
    result = make_result_binary(result=result)
    return jsonify({"Result" : result})
   except:
       return jsonify({"Result" : "An Error Occurred"})



if __name__ == "__main__":

    __model = return_model()

    app.run(host='0.0.0.0',port=5000)
