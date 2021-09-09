import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data2.csv')
ages = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)
# plt.yscale("log") # two methods to use log data
# count all occurrences of each age, divided into columns of bins
# plotting data in y axis in log help ...
median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
