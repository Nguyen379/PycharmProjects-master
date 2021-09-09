import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

s_re = pd.read_csv("voice.csv")
s_re.label = s_re.label.apply(lambda x: 1 if x == "male" else 0)
X_train, X_test, y_train, y_test = train_test_split(s_re.drop(columns=["label"]), s_re.label)
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))
