import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

"y = ax^2 + bx + c"
data = pd.read_csv('data_square.csv').values
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

lr_lst = [3e-12]
numIter = 5000
cost = np.zeros((numIter, 1))

for lr in lr_lst:
    N = data.shape[0]
    fig, (ax1, ax2) = plt.subplots(1, 2)
    x = np.stack([x, np.square(x)], axis=-1).reshape(30, 2)
    x = np.hstack((np.ones((30, 1)), x))
    w = np.array([1, -1, 1]).reshape(-1, 1)
    for i in range(0, numIter):
        r = np.dot(x, w) - y
        cost[i] = 0.5 * np.sum(r * r)
        w = w - lr * np.dot(x.T, r)
        print('step {}, w: {}'.format(i, w))
    ax1.plot(cost)

    predict = np.dot(x, w)
    x = data[:, 0].reshape(-1, 1)
    y = data[:, 1].reshape(-1, 1)
    ax2.plot(x[:, 0], predict, "r")
    ax2.scatter(x, y)

N = x.shape[0]
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)
x = np.stack([x, np.square(x)], axis=-1)
x = x.reshape(x.shape[0], x.shape[-1])
reg = LinearRegression().fit(x, y)
print(reg.coef_)
print(reg.intercept_)
a = []
b = []
for i in range(30, 100, 5):
    j = reg.coef_[0][0] * i + reg.coef_[0][1] * i * i + reg.intercept_
    a.append(i)
    b.append(j)

plt.scatter(a, b, c='r')

plt.show()
