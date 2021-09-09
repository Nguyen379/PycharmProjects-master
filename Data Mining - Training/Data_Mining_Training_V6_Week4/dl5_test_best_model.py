import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model

CATERGORIES = ["Cat", "Dog"]


def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = load_model("0_dense_128_layer_3_conv")
prediction = model.predict([prepare("dog.jpg")])
print(CATERGORIES[int(prediction[0][0])])
prediction = model.predict([prepare("cat.jpg")])
print(CATERGORIES[int(prediction[0][0])])
