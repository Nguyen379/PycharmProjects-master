from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
# Bar Chart 2: using info from csv

plt.style.use('fivethirtyeight')
sal = pd.read_csv("data.csv")
dict_common_jobs = Counter()
dict_common_jobs.update(sal["JobTitle"])
job_title = []
number = []
for n in dict_common_jobs.most_common(15):
    job_title.append(n[0])
    number.append(n[1])
print(job_title)
print(number)
job_title.reverse()
number.reverse()
plt.barh(job_title, number)

plt.xlabel('Number of jobs')
plt.title('Common jobs')

plt.tight_layout()

plt.show()
