import pandas as pd

df = pd.DataFrame({1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]},
                  index=['d', 'e', 'f', "g", "h", "i", "k", "l", "m", "n", "o", "p", "q"])
print(df[:2])

