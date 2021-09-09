import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, SpatialDropout1D, Conv1D, MaxPooling1D
from keras.layers.embeddings import Embedding
import pickle
from tensorflow.keras.callbacks import TensorBoard
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import time

max_review_len = 2293
max_features = 8178
len_train_file = 14375


NAME = time.time()
tensorboard = TensorBoard(log_dir=f'logs_RNN_count/{NAME}')
X = pickle.load(open("X_combined_c.pickle", "rb"))
y_train = pickle.load(open("y_train_c.pickle", "rb"))
y_test = pickle.load(open("y_test_c.pickle", "rb"))


# X = X.toarray()
y_train = np.reshape(y_train, (-1, 1))
y_test = np.reshape(y_test, (-1, 1))
print(X.shape)
print(y_train.shape)
print(y_test.shape)

X_train, X_test = X[:len_train_file], X[len_train_file:]
dense_output = len(np.unique(y_train))
model = Sequential()

model.add(Embedding(max_features, 50, input_length=max_review_len))
# model.add(SpatialDropout1D(0.2)
model.add(Conv1D(filters=50, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(Conv1D(filters=50, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(Conv1D(filters=50, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))

model.add(Dense(128, activation="relu"))
model.add(Dense(dense_output, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", metrics=["accuracy"], optimizer="adam")
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=64, callbacks=[tensorboard])

# 225/225 [================] - 1123s 5s/step - loss: 2.8427 - accuracy: 0.1672 - val_loss: 2.0848 - val_accuracy: 0.3206
# Epoch 2/10
# 225/225 [================] - 1015s 5s/step - loss: 1.8263 - accuracy: 0.3777 - val_loss: 1.6090 - val_accuracy: 0.4520
# Epoch 3/10
# 225/225 [================] - 1066s 5s/step - loss: 1.2374 - accuracy: 0.5610 - val_loss: 1.1793 - val_accuracy: 0.6048
# Epoch 4/10
# 225/225 [================] - 1087s 5s/step - loss: 0.9327 - accuracy: 0.6779 - val_loss: 1.0088 - val_accuracy: 0.6745
# Epoch 5/10
# 225/225 [================] - 1024s 5s/step - loss: 0.7114 - accuracy: 0.7568 - val_loss: 0.9726 - val_accuracy: 0.6875
# Epoch 6/10
# 225/225 [================] - 1031s 5s/step - loss: 0.5903 - accuracy: 0.8011 - val_loss: 0.9693 - val_accuracy: 0.7088
# Epoch 7/10
# 225/225 [================] - 1055s 5s/step - loss: 0.5265 - accuracy: 0.8280 - val_loss: 0.9129 - val_accuracy: 0.7355
# Epoch 8/10
# 225/225 [================] - 1047s 5s/step - loss: 0.4445 - accuracy: 0.8557 - val_loss: 0.9427 - val_accuracy: 0.7372
# Epoch 9/10
# 225/225 [================] - 1044s 5s/step - loss: 0.3702 - accuracy: 0.8856 - val_loss: 0.9297 - val_accuracy: 0.7467
# Epoch 10/10
# 225/225 [================] - 1045s 5s/step - loss: 0.3092 - accuracy: 0.9001 - val_loss: 0.9667 - val_accuracy: 0.7449

