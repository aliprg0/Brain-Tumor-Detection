from flask import Flask, request, render_template, jsonify
from utils import *
from flask_cors import CORS
import cv2
from PIL import Image
import numpy
from keras.models import load_model

app = Flask(__name__)
CORS(app)

__model = None

def  make_final_result(result):
   if result >= 0.5:
      return "Infected"
   else:
      return "OK"

def predict_the_pic(picture):
   
   image = cv2.imread(picture)
   image = Image.fromarray(image)
   image = image.resize((128, 128))
   img = numpy.array(image)
   inp_img = numpy.expand_dims(img, axis=0)
   rresult = __model.predict(inp_img)
   return rresult



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():

    try:

        data = request.files["myFile"]

        address = data.filename
        data.save(f"/app/data/{address}")

        result = predict_the_pic(f"/app/{data.filename}")

        result = make_final_result(result=result)

        return jsonify({"Result": f"{result}"})
    except:
        return jsonify({"Result": "An Error Occurred"})


if __name__ == "__main__":
    __model = load_model("/app/BrainTumorDetection.h5")
    app.run()
