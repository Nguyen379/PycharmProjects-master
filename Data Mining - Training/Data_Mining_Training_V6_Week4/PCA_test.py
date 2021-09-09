from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC
import pandas as pd

iris = load_iris()
# print(dir(iris))
# print(iris.target)
# print(iris.target_names)
# print(iris.feature_names)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
X, y = df.drop(["target"], axis=1), df["target"]

# pca = PCA().fit(X)
# print(pca.explained_variance_ratio_)
# plt.plot(np.cumsum(pca.explained_variance_ratio_))
# plt.xlabel('number of components')
# plt.ylabel('cumulative explained variance')
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y)
print(X_train.shape)
model = SVC(C=10)
clf = model.fit(X_train, y_train)
print(clf.score(X_test, y_test))  # 1

pca = PCA(n_components=1)
X = pca.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)
print(X_train.shape)
model = SVC(C=10)
clf = model.fit(X_train, y_train)
print(clf.score(X_test, y_test))  # 0.92
"PCA giảm số cột từ 4 xuống 1 trong khi accuracy giảm từ 1 => 0.92"

