from flask import Flask, request, render_template, jsonify
from utils import *


app = Flask(__name__)
__model = None


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
   try:
     data = request.files["myFile"]
     data.save(f"data/{data.filename}")
     result = predict_the_pic(f"data/{data.filename}", model=__model)
     result = make_final_result(result=result)
     return jsonify({"Result": result})
   except:
      return jsonify({"Result" : "An Error Occurred"})


if __name__ == "__main__":

    __model = return_model()

    app.run()
