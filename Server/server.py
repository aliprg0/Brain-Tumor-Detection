from flask import Flask,request,render_template,jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["Post"])
def predict():
   pic = request.files.get("inpFile")
   print("Done")


if __name__ == "__main__":
    app.run(threaded=True,debug=True)
    print("Server Started...")