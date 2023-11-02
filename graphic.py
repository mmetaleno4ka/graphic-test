import matplotlib.pyplot as plt
import numpy as np

def calculate_distance(v0, a, t):
    distance = v0 * t + 0.5 * a * t**2
    return distance

v0 = int(input("Введіть початкову швидкість v0: "))
a = int(input("Введіть прискорення a: "))

time_values = range(0, 21)  

distances = [calculate_distance(v0, a, t) for t in time_values]

plt.plot(time_values, distances, marker='^', linestyle='-.')
plt.xlabel('t')
plt.ylabel('S')
plt.grid(True)

plt.show()