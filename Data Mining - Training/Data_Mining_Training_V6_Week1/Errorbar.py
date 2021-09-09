import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

fig, ax = plt.subplots(1)
ax.errorbar(x, y, yerr=dy, marker='o', linestyle='', color='black', ecolor='lightgray', elinewidth=3, capsize=0)
# also xerr=...
plt.tight_layout()
plt.show()
