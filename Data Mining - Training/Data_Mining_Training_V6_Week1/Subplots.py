from matplotlib import pyplot as plt
import pandas as pd
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)  # share=True
# 2 rows: 2 plots on each row => ax1 and ax2 represent each
# sharex: share x-axis values
# fig2, ax2 = plt.subplots() to create anoher window
# create instances
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')
