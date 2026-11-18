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

print("Центральный фрагмент:\n", temperatures[0:2, 1:3])
print("Форма центрального фрагмента:", temperatures[0:2, 1:3].shape)

# Задание 4
print("\n\n")
matrix = np.arange(1, 26).reshape(5, 5)

print("Первые три строки:\n", matrix[:3])
print("Shape:",matrix[:3].shape, "\n")

print("Последние две строки:\n", matrix[-2:])
print("Shape:", matrix[-2:].shape, "\n")

print("Первые два столбца:\n", matrix[:, :2])
print("Shape:", matrix[:, :2].shape, "\n")

print("Фрагмент (строки 1–3, столбцы 2–4):\n", matrix[1:4, 2:5])
print("Shape:", matrix[1:4, 2:5].shape, "\n")

print("Угловой блок 2x2 в правом нижнем углу:\n", matrix[-2:, -2:])
print("Shape:", matrix[-2:, -2:].shape)

# Задание 5
print("\n\n")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после замены:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после замены:\n", small_matrix, "\n")

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours, "\n")

changed_matrix = matrix.copy()
changed_matrix[1] = 0          
changed_matrix[:, -1] = -1     
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)