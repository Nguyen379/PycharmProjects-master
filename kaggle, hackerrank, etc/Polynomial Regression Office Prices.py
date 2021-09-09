import numpy as np
F, N = map(int, input().split(" "))
train = np.array([input().split(" ") for _ in range(N)], float)
T = int(input())
test = np.array([input().split(" ") for _ in range(T)], float)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

model = LinearRegression()
poly_features = PolynomialFeatures(3, include_bias=False)
model.fit(poly_features.fit_transform(train[:, :-1]), train[:, -1])

y_pred = model.predict(poly_features.fit_transform(test))
print(*y_pred, sep="\n")
