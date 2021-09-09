import numpy as np

"""Buoi 1: Numpy"""
# Axis 0 will act on all the ROWS in each COLUMN
# Axis 1 will act on all the COLUMNS in each ROW

a = np.array([[1, 2, 3, 4, 5]], dtype='float32')
print(type(a))
print(a.shape)
print(a)

b = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], ndmin=5)
# each [] represent a dimension
# ndmin is the minimum dimension
print(b.shape)
print(b[0, 0, 0, 1], b[0, 0, 0, 0, 1])
print(b.flatten())
print('\n')

c = np.zeros((3, 4), dtype=int)
print(c)

d = np.full((3, 4), 3.14)
print(d)

e = np.eye(3, 4, k=0)
# fill diagonal k of matrix row x column with values of 1 while others are 0
print(e)

f = np.array([n for n in range(0, 10, 2)])
g = np.arange(0, 10, 2)
print(f)
print(g)
print('\n')

# Ma tran chuyen vi
h1 = np.array([1, 2, 3])
print(h1.T)
h2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(h2)
print(h2.T)
print(h2.reshape(1, 9))
print('\n')

matrix_b = np.array([[3, -4, 5], [2, -3, 1], [3, -5, 1]])
print(matrix_b.diagonal())
print(matrix_b.diagonal().sum())
inverted_matrix_b = np.linalg.inv(matrix_b)
print(np.round(inverted_matrix_b, 2))

matrix_c = np.array([[1, 3, 5, -1], [2, -1, -1, 4], [5, 1, -1, 7], [7, 7, 11, 1]])
print(np.linalg.matrix_rank(matrix_c))
print(matrix_c)
print(np.max(matrix_c, axis=1))
print(np.min(matrix_c))

ma = np.array([[1, -3, 2], [2, 1, -1], [0, 3, -2]])
mc = np.array([[-1, 0], [2, 0], [1, 1]])
print(ma @ mc)

i = np.eye(3)
result = np.eye(2)
matrix_p = np.array([[0.66253149, 0.17765876], [0.60264879, 0.33166751]])

for _ in range(3):
    result = result @ matrix_p

print(result)

matrix_c = np.array([[1, 3, 5, -1], [2, -1, -1, 4], [5, 1, -1, 7], [7, 7, 11, 1]])
print(matrix_c[:3, 0:3])
# ":3": first 3 lines. "0:3": column 1 to 3

print(matrix_c[1, :], matrix_c[1, :].shape)
print(matrix_c[:, 1], matrix_c[:, 1].shape)
# integer indexing returns lower-ranked matrix

print(matrix_c[1:2, :], matrix_c[1:2, :].shape)
print(matrix_c[:, 1:2], matrix_c[:, 1:2].shape)
# slice indexing returns original-ranked matrix

print('\n')

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.arange(4)
c = np.array([0, 1, 2, 1])
print(a[b, c])

# boolean
print(a > 2)
# matrix values of true and false
print(a[a > 2])

# mathematical operations
d = np.array([[11, 2, 3], [4, 51, 6], [7, 8, 19], [10, 11, 2]])
e = np.array([[11, 2, 3], [4, 51, 6], [7, 8, 19]])
g = np.array([1, 0, 1])

print(np.add(a, d))
print(a + d)
print(np.subtract(a, d))
print(a - d)

print('\n')
print(np.multiply(a, d))
print(a * d)
# caution: this is NOT matrix multiplication

print(a.dot(e))
print(a @ e)
# this IS matrix multiplication


print('\n')
print(np.divide(a, d))
print(np.sqrt(a))

print('\n')
print(np.sum(a))
print(np.sum(a, axis=0))
# sum each column
print(np.sum(a, axis=1))
# sum each row

f = np.random.rand(100)
print(np.argmax(a))
print(a.argmax())
# np.:sum, prod, mean, std, var, min, max, argmin, argmax, median, percentile, any, all
print(np.max(d, axis=0))
# max each column
print(np.max(d, axis=1))
# max each row

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
vr = np.vectorize(lambda x: x + 2)
print(vr(a))
print(np.vectorize(lambda x: x + 2)(a))
# vectorize giong map: unpack r chay qua func

from sklearn.feature_extraction import DictVectorizer

data_dict = [{'Red': 2, 'Blue': 4},
             {'Red': 4, 'Blue': 3},
             {'Red': 1, 'Yellow': 2},
             {'Red': 2, 'Yellow': 2}]
dict_vect = DictVectorizer(sparse=False)
# dict_vect is an object of class DictVectorizer
features = dict_vect.fit_transform(data_dict)
# fit_transform is method that takes in values from data_dict and put it into object
print(features)
print(dict_vect.get_feature_names())

"""Buoi 2: Pandas"""
import pandas as pd
import numpy as np

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# print(data.index)
# print(data[1])
# print(data.max())

# data1 = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[2, 4, 6, 2, 1])
# print(data1[4])
# print(data1[6])

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995}
area = pd.Series(area_dict)
print(population)
states = pd.DataFrame({'population': population, 'area': area})
print(states)
print(states.index)
print(states.columns)
print(states.head(3))
print(states.tail(2))
print(states.info())
print(states.describe())
print(population['California'])
print(states['area'])
print(dir(states))
states_copy = states.copy()
states_copy.rename(columns={'area': 'areas'}, inplace=True)
# inplace accepts changes
print(states_copy)
print(states.loc['Texas':'Florida'])
# index duoc khai bao
print(states.iloc[1:3])
# index mac dinh
states.applymap(np.log)
# np.log: function
# np.log(): function.invocation
# axis = 0 apply function to each column, = 1 apply function to each row
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [10, 20, 30, 40],
                   'C': [20, 40, 60, 80]
                   },
                  index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])


def custom_sum(row):
    return row.sum()


df["column"] = df.apply(custom_sum, axis=1)
df.loc["row"] = df.apply(custom_sum, axis=0)
print(df)
print(df.apply(custom_sum, axis=1))
print(df.apply(custom_sum, axis=0))

# apply: used to modify dataframe itself
# applymap: used to apply changes to elements of dataframe
