import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "C:\\Users\\Asus\\PycharmProjects\\Data Mining - Training\\Data_Mining_Training_V6_Week4\\PetImages"
CATEGORIES = ["Dog", "Cat"]

# for dir, subdir, filenames in os.walk(DATADIR):
#     for filename in filenames:
#         path = os.path.join(dir, filename)
#         img_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#         plt.matshow(img_array, cmap='gray')
#         plt.show()
#         break


training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                IMG_SIZE = (50, 50)
                new_array = cv2.resize(img_array, IMG_SIZE)
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

            # plt.matshow(new_array, cmap="gray")
            # plt.show()


create_training_data()
print(len(training_data))

import random
random.shuffle(training_data)
X = []
y = []
for feature, label in training_data:
    X.append(feature)
    y.append(label)
X = np.array(X).reshape(-1, 50, 50, 1)

import pickle
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

print(type(X))
print(X.shape)
