from flask import Flask, request, render_template, jsonify
from utils import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
__model = None


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
     num = 0
   #try:
     
     data = request.files["myFile"]
     num=num + 1
     address = f"data/{data.filename}"
     data.save(address)
     num=num + 1
     result = predict_the_pic(address, model=__model)
     num=num + 1
     result = make_final_result(result=result)
     num=num + 1
     return jsonify({"Result": f"result. Code : {num}"})
  # except:
  #    return jsonify({"Result" : f"An Error Occurred.\n Code : {num}"})


if __name__ == "__main__":

    __model = return_model()

    app.run()
