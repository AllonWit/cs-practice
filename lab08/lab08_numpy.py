import numpy as np;

# Задание 1
hours = np.arange(0 , 22 , 3)
line = np.linspace(0 , 1 , 5)
zeros = np.zeros(6 , dtype=int)
unknown_table = np.full((2 ,3) , -1)
identity = np.eye(3)

print(f"hours = {hours}")
print(f"line = {line}")
print(f"zeros = {zeros}")
print(f"unknown_table = {unknown_table}")
print(f"identity = {identity}")

# Задание 2

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])