import numpy as np
from matplotlib import pyplot as plt

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.7, bins=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              range=np.arange(0, 400, 50))

fig, ax = plt.subplots(1)
ax.hist(x1, **kwargs)
ax.hist(x2, **kwargs)
ax.hist(x3, **kwargs)

plt.tight_layout()
plt.show()
