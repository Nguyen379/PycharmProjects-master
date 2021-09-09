import pandas as pd
import numpy as np
train_data = pd.read_csv("train.csv")
train_data.Age.fillna(train_data.Age.mean(), inplace=True)
print(train_data.Age)

print(type(train_data.iloc[[888]]))
print(type(train_data.iloc[888]))

