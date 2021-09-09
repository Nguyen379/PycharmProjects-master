import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Asus\Downloads\AI4E\test_dau_vao\data_linear.csv")
# print(df.head())
df.plot.scatter(x="Diện tích", y="Giá")

data = pd.read_csv('data_linear.csv').values
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)
plt.scatter(x, y)
plt.xlabel("Dien tich")
plt.ylabel("Gia")


lr_lst = [1e-10, 5e-8, 1e-6, 2e-4, 5e-2, 0.1]
numIter = 100
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

plt.tight_layout()
plt.legend()
plt.show()
