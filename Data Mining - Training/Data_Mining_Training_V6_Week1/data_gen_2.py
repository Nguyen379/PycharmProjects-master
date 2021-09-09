import pandas as pd
import time
import random
x = 0
y = 1000
y2 = 1000
data = {"x": [x], "y": [y], "y2": [y2]}
df = pd.DataFrame(data=data, columns=["x", "y", "y2"])
print(df)
df.to_csv("data_gen.csv")
while True:
    x += 1
    y += random.randint(-6, 8)
    y2 += random.randint(-5, 6)
    data2 = {"x": [x], "y": [y], "y2": [y2]}
    df2 = pd.DataFrame(data=data2, columns=["x", "y", "y2"])
    df = df.append(df2)
    print(df)
    df.to_csv("data_gen.csv")
    time.sleep(1)
