import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

iris = load_iris()
print(iris.data[:, :2]) # first 2 features only
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target  # target's values (0,1,2) represent iris' name in target_names
df["flower_name"] = df["target"].apply(lambda x: iris.target_names[x])

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

fig1, (ax1,ax2) = plt.subplots(ncols=1, nrows=2, figsize=(7, 7), sharex=True)

ax1.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], c=df0["petal length (cm)"], cmap="summer")
ax1.scatter(df1["sepal length (cm)"], df1["sepal width (cm)"], c=df1["petal length (cm)"], cmap="summer")
cbar1 = fig1.colorbar(ax=ax1, mappable=plt.cm.ScalarMappable(cmap='summer'))

cbar1.set_label('Petal length ratio')
ax1.set_title('Iris 0 vs 1')
ax1.set_xlabel('Sepal length')
ax1.set_ylabel('Sepal width')

ax2.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], c=df0["petal length (cm)"], cmap="summer")
ax2.scatter(df2["sepal length (cm)"], df2["sepal width (cm)"], c=df2["petal length (cm)"], cmap="summer")
cbar2 = fig1.colorbar(ax=ax2, mappable=plt.cm.ScalarMappable(cmap='summer'))

cbar2.set_label('Petal length ratio')
ax2.set_title('Iris 0 vs 2')
ax2.set_xlabel('Sepal length')
ax2.set_ylabel('Sepal width')
# ax2.set_xlim([-1, 11])
# ax2.set_ylim([-1.5, 1.5])
plt.tight_layout()
plt.show()
