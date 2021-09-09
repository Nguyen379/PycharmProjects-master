# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?fbclid=IwAR00Gpuf2lVZ777HE6tfk7NL5qzsx9O1djqhmDrzP2f4iWgfbr-PwNRsAwQ
import math
import numpy as np
physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
p_mean = np.mean(physics)
h_mean = np.mean(history)

tu_so_physics = [p - p_mean for p in physics]
tu_so_history = [h - h_mean for h in history]
tu_so = 0
for p, h in zip(tu_so_physics, tu_so_history):
    tu_so += p*h

mau_physics = sum([p**2 for p in tu_so_physics])
mau_history = sum([h**2 for h in tu_so_history])
mau_so = math.sqrt(mau_physics*mau_history)

r = tu_so/mau_so
print(round(r, 3))

# for hackerrank
physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
p_mean = sum(physics)/len(physics)
h_mean = sum(history)/len(history)

tu_so_physics = [p - p_mean for p in physics]
tu_so_history = [h - h_mean for h in history]
tu_so = 0
mau_physics = 0
mau_history = 0
for p, h in zip(tu_so_physics, tu_so_history):
    tu_so += p*h
    mau_physics += p**2
    mau_history += h**2
mau_so = (mau_physics*mau_history)**(1/2)

r = tu_so/mau_so
print(round(r, 3))
