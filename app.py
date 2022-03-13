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
     
   #try:
     
     data = request.files["myFile"]
     
     address = data.filename
     data.save(address)
    

     result = predict_the_pic(f"/app/{data.filename}")

     result = make_final_result(result=result)
    
     return jsonify({"Result": f"{result}"})
  # except:
  #    return jsonify({"Result" : f"An Error Occurred.\n Code : {num}"})


if __name__ == "__main__":


    app.run()
