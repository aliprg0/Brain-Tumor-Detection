from keras.models import load_model
import cv2
from PIL import Image
import numpy




def return_model():
     model = load_model("BrainTumorDetection.h5")
     return model

def  make_final_result(result):
   if result >= 0.5:
      return "Infected"
   else:
      return "OK"


def predict_the_pic(picture,model):

   image = cv2.imread(picture)
   image = Image.fromarray(image)
   image = image.resize((128, 128))
   img = numpy.array(image)
   inp_img = numpy.expand_dims(img, axis=0)
   rresult = model.predict(inp_img)
   return rresult
