import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

"y = ax + b"
# df = pd.read_csv(r"data_square.csv")
# print(df.head())
# df.plot.scatter(x="Diện tích", y="Giá nhà")


data = pd.read_csv('data_square.csv').values
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

lr_lst = [1e-5]
numIter = 100000
cost = np.zeros((numIter, 1))
for lr in lr_lst:
    fig, (ax1, ax2) = plt.subplots(1, 2)
    N = data.shape[0]
    x = np.hstack((np.ones((N, 1)), x))
    w = np.array([0, 1]).reshape(-1, 1)
    for i in range(0, numIter):
        r = np.dot(x, w) - y
        cost[i] = 0.5*np.sum(r*r)
        w = w - lr * np.dot(x.T, r)
        print('step {}, cost: {}'.format(i, cost[i]))
    ax1.plot(cost)

    print(w)
    predict = np.dot(x, w)
    ax2.plot((x[0][1], x[N-1][1]), (predict[0], predict[N-1]), "r")
    plt.title("Fitting Graph to data")
    x = data[:, 0].reshape(-1, 1)
    y = data[:, 1].reshape(-1, 1)
    ax2.scatter(x, y)
    fig.suptitle(f"Graph of learning rate: {lr}")

N = x.shape[0]
reg = LinearRegression().fit(x, y)
predict = reg.predict(x)
plt.plot((x[0][0], x[N-1][0]), (predict[0], predict[N-1]), 'r')
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)
print(reg.coef_)
print(reg.intercept_)
plt.scatter(x, y)
plt.xlabel('mét vuông')
plt.ylabel('giá')
plt.show()


