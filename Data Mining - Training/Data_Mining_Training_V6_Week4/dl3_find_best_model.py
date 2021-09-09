import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import time
import pickle
import numpy as np

X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle", "rb"))
X = np.array(X / np.amax(X[0]))
y = np.array(y)

dense_layers = [0, 1] # [0, 1, 2]
layer_sizes = [64, 128] # [32, 64, 128]
conv_layers = [2, 3] # [1, 2, 3]
for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = f"{dense_layer}_dense_{layer_size}_layer_{conv_layer}_conv_{int(time.time())}"
            tensorboard = TensorBoard(log_dir=f'logs/{NAME}')
            print(NAME)
            model = Sequential()

            model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            for n in range(conv_layer - 1):
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation("relu"))
                model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())
            for n in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation("relu"))

            model.add(Dense(1))
            model.add(Activation("sigmoid"))

            model.compile(loss="binary_crossentropy",
                          optimizer="adam",
                          metrics=["accuracy"])

            model.fit(X, y, batch_size=128, epochs=10, validation_split=0.3, callbacks=[tensorboard])

# tensorboard --logdir="C:\Users\Asus\PycharmProjects\Data Mining - Training\Data_Mining_Training_V6_Week4\logs"
# best is lowest val_loss
