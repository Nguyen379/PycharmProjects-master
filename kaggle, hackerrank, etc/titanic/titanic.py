import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler

plt.style.use('fivethirtyeight')
sns.set(style='whitegrid', color_codes=True)

for root, directory, file in os.walk("/kaggle, hackerrank, etc"):
    for f in file:
        print(os.path.join(root, f))

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

df = train_data.copy()
df2 = test_data.copy()

print(df.isnull().mean())
# cabin = 0.77 => drop cabin


df.Age.fillna(df.Age.mean(), inplace=True)
df2.Age.fillna(df2.Age.mean(), inplace=True)

df2.Fare.fillna(df2.Fare.mean(), inplace=True)

df_cor = df.drop(columns=["Name", "Ticket", "Cabin", "Embarked"]).corr()
mask = np.array(df_cor)
mask[np.tril_indices_from(mask)] = False
sns.heatmap(data=df_cor, mask=mask, square=True, annot=True)


# print(df.iloc[:, 1:5])
# ":": all rows, "1:5": column 1 to 5


def calc_limit(feature, first_quartile_range, third_quartile_range):
    down, up = df[feature].quantile([first_quartile_range, third_quartile_range])
    iqr = up - down
    return down - 1.5 * iqr, up + 1.5 * iqr


def plot(feature, first_quartile_range, third_quartile_range):
    sns.boxplot(data=df, x=feature)
    down, up = calc_limit(feature, first_quartile_range, third_quartile_range)
    plt.xlabel(feature)
    # plt.legend()
    # plt.show()
    return down, up


# drop outliers
for n in ["Age", "Fare"]:
    down, up = plot(n, 0.25, 0.75)
    df = df[(df[n] < up) & (df[n] > down)]

# cap outliers
# for n in ["Age","Fare"]:
#     down, up = plot(n, 0.1, 0.9)
#     df.loc[df[n] > up] = up
#     df.loc[df[n] < down] = down


X = pd.get_dummies(df.drop(columns=["Name", "Cabin", "Survived", "Ticket"]))
y = df.Survived
X_test = pd.get_dummies(df2.drop(columns=["Name", "Cabin", "Ticket"]))

sc = StandardScaler()
sc.fit(X)
sc.transform(X)

sc2 = StandardScaler()
sc2.fit(X_test)
sc2.transform(X_test)

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
y_pred = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df2.PassengerId, "Survived": y_pred})
output.to_csv('my_submission.csv', index=False)
