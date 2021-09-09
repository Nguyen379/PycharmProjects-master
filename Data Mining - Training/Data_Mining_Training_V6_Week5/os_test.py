import os
from pathlib import Path
print("\"")
a = r"E:\PycharmProjects\Data Mining - Training"
b = r"Data_Mining_Training_V6_Week5"
c = r"\Data_Mining_Training_V6_Week5"
print(os.path.join(a, b))
print(os.path.join(a, c))
print()
for a1, a2, a3 in os.walk(os.path.join(a, b)):
    print(a1)
    print(a2)
    print(a3)
    print()

a = Path(a)
for x in (a/b).iterdir():
    print(x)
    # print(x.read_text()) for raw file
