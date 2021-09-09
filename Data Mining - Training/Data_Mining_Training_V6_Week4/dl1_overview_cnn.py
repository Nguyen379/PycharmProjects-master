import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1) # hoi sau
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28))) # input layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # first hidden layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # second hindden layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax)) # output layer

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
model.fit(x_train, y_train, epochs=3)
val_loss, val_acc = model.evaluate(x_test, y_test)
predictions = model.predict([x_test])
print(predictions)
print(np.argmax(predictions[0]))

plt.imshow(x_test[0])
plt.show()
