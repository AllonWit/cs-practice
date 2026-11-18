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
print("\n\n")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Обратный порядок:", hours[::-1])

# Задание 3
print("\n\n")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(f"форма: {temperatures.shape}")
print(f"число измерений: {temperatures.ndim}")
print(f"число элементов: {temperatures.size}")

print(f"Значение из второй строки и третьего столбца: {temperatures[1 , 2]}")

print(f"первую строку: {temperatures[0]}")

print(f"первую строку: {temperatures[ :, -1]}")

print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

center = temperatures[0:2, 1:3]
print("Центральный фрагмент:\n", center)
print("Форма центрального фрагмента:", center.shape)