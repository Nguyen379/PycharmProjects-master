import pandas as pd
import numpy as np
import math
import string
from collections import Counter

'''Bai 2'''
# np.log là object function, np.log() là function invocation
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})


def get_log(x):
    return math.log(x)


print(data)
print(data.applymap(np.log))
print(data.applymap(math.log))
print(data.applymap(lambda x: math.log(x)))
print(data.applymap(get_log))

# 2
sal = pd.read_csv("Salaries.csv")
print(sal.head())
# 3
print(sal.head())
# 4
print(sal.info())
# 5
sum_base_pay = 0
for n in sal["BasePay"].dropna():
    sum_base_pay += n
average = sum_base_pay / len(sal["BasePay"].dropna())
print(average)

average2 = sal["BasePay"].mean()
# 6
largest_overtime_pay = 0
for n in sal["OvertimePay"].dropna():
    if n > largest_overtime_pay:
        largest_overtime_pay = n
print(largest_overtime_pay)
print(sal['OvertimePay'].max())

# 7, 8
a = sal.loc[sal['EmployeeName'] == "JOSEPH DRISCOLL"]
print(a["JobTitle"])
combined_a = sal.loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL', 'JobTitle']
print(combined_a)
combined_a_2 = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print(combined_a_2)
print(a["TotalPayBenefits"])

# 9
highest_paid = 0
for n in sal['TotalPayBenefits']:
    if n > highest_paid:
        highest_paid = n
b = sal.loc[sal["TotalPayBenefits"] == highest_paid]
print(b["EmployeeName"])

print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])

# 10
lowest_paid = 999999
for n in sal["TotalPayBenefits"]:
    if n < lowest_paid:
        lowest_paid = n
c = sal.loc[sal["TotalPayBenefits"] == lowest_paid]
print(c["EmployeeName"])

# 11
sum_pay_2011 = 0
division_2011 = 0
sum_pay_2012 = 0
division_2012 = 0
sum_pay_2013 = 0
division_2013 = 0
sum_pay_2014 = 0
division_2014 = 0

for n in sal["BasePay"].dropna():
    m = sal.loc[sal["BasePay"] == n]
    if m["Year"].to_string(index=False) == ' 2011':
        sum_pay_2011 += n
        division_2011 += 1
    elif m["Year"].to_string(index=False) == ' 2012':
        sum_pay_2012 += n
        division_2012 += 1
    elif m["Year"].to_string(index=False) == ' 2013':
        sum_pay_2013 += n
        division_2013 += 1
    elif m["Year"].to_string(index=False) == ' 2014':
        sum_pay_2014 += n
        division_2014 += 1
average_pay_2011 = sum_pay_2011 / division_2011
average_pay_2012 = sum_pay_2012 / division_2012
average_pay_2013 = sum_pay_2013 / division_2013
average_pay_2014 = sum_pay_2014 / division_2014

print(average_pay_2011)  # 58537.52171990339
print(average_pay_2012)  # 59596.41675378191
print(average_pay_2013)  # 61950.19791424823
print(average_pay_2014)  # 59270.32652740981
# chay mat 5 phut cuoc doi=))
# cach 2
print(sal.groupby('Year')['BasePay'].mean())

# 12
unique_jobs = []
for n in sal['JobTitle']:
    if n not in unique_jobs:
        unique_jobs.append(n)
print(len(unique_jobs))
print(sal['JobTitle'].nunique())
# 13
dict_common_jobs = {}
for n in sal["JobTitle"]:
    if n not in dict_common_jobs:
        dict_common_jobs[n] = 1
    elif n in dict_common_jobs:
        dict_common_jobs[n] += 1
print(sorted(dict_common_jobs, key=lambda x: dict_common_jobs[x])[-5:])
# sorted_dict_common_jobs = {k: v for k, v in sorted(dict_common_jobs.items(), key=lambda item: item[1])}
# use above for full list with numbers

dict_common_jobs = Counter()
dict_common_jobs.update(sal["JobTitle"])
print(dict_common_jobs)

print(sal['JobTitle'].value_counts().head(10))
print(sal["JobTitle"].value_counts().tail(10))
print(sal["JobTitle"].value_counts(ascending=True).head(10))
# 14
one_person_jobs = []
# sal.loc lat tat ca gia tri thoa man dieu kien
for n in sal.loc[sal["Year"] == 2013]['JobTitle'].dropna():
    m = len(sal.loc[sal["JobTitle"] == n])
    if m == 1:
        one_person_jobs.append(n)
    else:
        pass
print(one_person_jobs)
# ['Managing Attorney', 'Civil Case Settlmnt Specialist',
# 'Captain, (Fire Department)', 'Public Safety Comm Tech',
# 'Drug Court Coordinator', 'IS Technician Assistant']
jobs = sal[sal['Year'] == 2013]['JobTitle'].value_counts()
print(jobs[jobs == 1].count())
# 15
chief_people = []
for n in sal["JobTitle"]:
    m = ''.join([tu for tu in list(n) if tu not in string.punctuation]).split()
    if "CHIEF" in m:
        a = sal.loc[sal["JobTitle"] == n]["EmployeeName"].to_string(index=False)
        for b in a.split("\n"):
            if b.strip() not in chief_people:
                chief_people.append(b.strip())
print(chief_people)

print(sal[sal['JobTitle'].str.contains('Chief')]['JobTitle'].count())

print(sum(sal['JobTitle'].str.contains('Chief')))

# ECom
ecom = pd.read_csv('EcommercePurchases.csv')
# How many people made the purchase during the AM and how many people made the purchase during PM ?
print(ecom['AM or PM'].value_counts())
# How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())
# Hard: How many people have a credit card that expires in 2025?
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))
# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
