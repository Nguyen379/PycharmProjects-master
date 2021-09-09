from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

# Pie chart
plt.style.use('fivethirtyeight')

slices = [1, 3, 2, 4]
labels = ["one", "three", 'two', "four"]
colors = ["yellow", "red", "blue", "green"]
explode = [0.1, 0, 0, 0]
plt.pie(slices, labels=labels, wedgeprops={"edgecolor": "black"}, colors=colors, explode=explode,
        shadow=True, startangle=120, autopct="%1.1f%%")

plt.title('Common jobs')

plt.tight_layout()

plt.show()
