# Importing resources
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import cv2
from PIL import Image
import numpy
from keras.models import load_model
import sqlite3

# initializing app
app = Flask(__name__)
CORS(app)


# loading AI Model
__model = load_model("/app/BrainTumorDetection.h5")


# this function make the result readlbe for humans after ai prediction
def make_final_result(result):
    if result >= 0.5:
        return "Infected"
    else:
        return "OK"

# open an analyze a send picture for tumor


def predict_the_pic(picture):
    image = cv2.imread(picture)
    image = Image.fromarray(image)
    image = image.resize((128, 128))
    img = numpy.array(image)
    inp_img = numpy.expand_dims(img, axis=0)
    rresult = __model.predict(inp_img)
    return rresult

# home page


@app.route("/")
def home():
    return render_template("index.html")

# api that the picture get send to for prediction


@app.route("/predict", methods=['POST'])
def predict():

    try:

        data = request.files["myFile"]

        address = data.filename
        data.save(f"/app/data/{address}")

        result = predict_the_pic(f"/app/data/{data.filename}")

        result = make_final_result(result=result)

        return jsonify({"Result": f"{result}"})
    except:
        return jsonify({"Result": "An Error Occurred"})

# info page


@app.route("/info/")
def return_info():
    return render_template("info.html")

# contact us page


@app.route("/contact/")
def return_contact_us_page():
    return render_template("contact_us.html")


# api for saving "contact_us_page" requests into database for reading
@app.route("/add_request")
def handle_contact():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("message")

    conn = sqlite3.connect('/app/requests.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS requests(
   email TEXT PRIMARY KEY,
   name TEXT,
   message TEXT);""")
    conn.commit()

    requ = (email, name, message)

    cur.execute("INSERT INTO requests VALUES(?, ?, ?);", requ)
    conn.commit()
    cur.close()
    conn.close()

    return "<p>Done! Thanks.If There Is A Problem, We'll Contact You. </p>", 200


# runs the server
if __name__ == "__main__":
    app.run()
