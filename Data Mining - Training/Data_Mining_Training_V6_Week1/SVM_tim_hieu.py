# training model: use the info to draw a graph
# testing model: check to see how well the graph
# bias: how well it fits training model, variant: how well it fits testing model

import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np

iris = load_iris()
print(iris.target_names)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target  # target's values (0,1,2) represent iris' name in target_names
df["flower_name"] = df["target"].apply(lambda x: iris.target_names[x])

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

df_cut = df.drop(["target", "flower_name"], axis="columns")
x_train, x_test, y_train, y_test = train_test_split(df_cut, df["target"], test_size=0.3)
model = SVC(C=10)
clf = model.fit(x_train, y_train)
print("{:.5f}".format(model.score(x_test, y_test)))


fig1, ax1 = plt.subplots(figsize=(10, 6))

ax1.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], c=df0["petal length (cm)"],
            cmap="Reds", label="Example No.0")
ax1.scatter(df1["sepal length (cm)"], df1["sepal width (cm)"], c=df1["petal length (cm)"],
            cmap="Blues", label="Example No.1")
ax1.scatter(df2["sepal length (cm)"], df2["sepal width (cm)"], c=df2["petal length (cm)"],
            cmap="Greens", label="Example No.2")

cbar1 = fig1.colorbar(ax=ax1, mappable=plt.cm.ScalarMappable(cmap='Greens'))
cbar1.set_label('Example No.2')
cbar2 = fig1.colorbar(ax=ax1, mappable=plt.cm.ScalarMappable(cmap='Blues'))
cbar2.set_label('Example No.1')
cbar3 = fig1.colorbar(ax=ax1, mappable=plt.cm.ScalarMappable(cmap='Reds'))
cbar3.set_label('Example No.0')

ax1.set_title('Iris 0 vs 1')
ax1.set_xlabel('Sepal length')
ax1.set_ylabel('Sepal width')

plt.xticks(np.arange(4, 9))
plt.tight_layout()
plt.show()

