import os
import cv2
import numpy as np
from tqdm import tqdm
import pickle

REBUILD_DATA = True
cat_dir = "C:\\Users\\Asus\\PycharmProjects\\Data Mining - Training\\Data_Mining_Training_V6_Week4\\PetImages\\Cat"
dog_dir = "C:\\Users\\Asus\\PycharmProjects\\Data Mining - Training\\Data_Mining_Training_V6_Week4\\PetImages\\Dog"


class DogsVSCats():
    def __init__(self):
        self.IMG_SIZE = 50
        self.cat_dir = "C:\\Users\\Asus\\PycharmProjects\\Data Mining - Training\\Data_Mining_Training_V6_Week4" \
                       "\\PetImages\\Cat"
        self.dog_dir = "C:\\Users\\Asus\\PycharmProjects\\Data Mining - Training\\Data_Mining_Training_V6_Week4" \
                       "\\PetImages\\Dog"
        self.training_data = []
        self.labels = ["Cats", "Dogs"]
        self.categorical_labels = {"Cats": 0, "Dogs": 1}
        self.count = {"Cats": 0, "Dogs": 0}

    def make_training_data(self):
        for label in self.labels:
            for path in tqdm(os.listdir(self.dog_dir)):
                try:
                    path = os.path.join(self.dog_dir, path)
                    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                    img = cv2.resize(img, (self.IMG_SIZE, self.IMG_SIZE))
                    self.training_data.append([np.array(img), np.eye(2)[self.categorical_labels[label]]])
                    self.count[label] += 1
                except Exception as e:
                    print(type(e))
                    print(e)
                    pass
        np.random.shuffle(self.training_data)
        with open("training_data", "wb") as f:
            pickle.dump(self.training_data, f)
        print(self.count)


dvc = DogsVSCats()
dvc.make_training_data()
