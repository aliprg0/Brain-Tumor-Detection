from keras.models import load_model
import cv2

model = load_model("BrainTumorDetection.h5")


image = cv2.imread("y36.jpg")

from PIL import Image

image = Image.fromarray(image)

image = image.resize((128,128))

import numpy

img = numpy.array(image)

inp_img = numpy.expand_dims(img,axis=0)

rresult = model.predict(inp_img)

print(rresult)