from matplotlib import pyplot as plt
import numpy as np
from matplotlib.legend import Legend
fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)
for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                     styles[i], color='black')

ax.axis('equal')

ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)

leg = Legend(ax, lines[2:], ['line C', 'line D'],
             loc='lower right', frameon=False)
ax.add_artist(leg)
