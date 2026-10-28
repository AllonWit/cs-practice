import numpy as np

def reshape_rows(values, width):
    if not values or width <= 0 or len(values) % width != 0:
        return []
    
    # Формируем матрицу заданной ширины
    matrix = np.array(values, dtype=float).reshape(-1, width)
    
    # Находим среднее для каждой строки (столбец средних значений)
    row_means = np.mean(matrix, axis=1, keepdims=True)
    
    # Создаем матрицу той же формы, заполненную средними значениями строк
    result = np.broadcast_to(row_means, matrix.shape)
    
    # Округляем до 6 знаков и возвращаем в виде списка списков
    return np.round(result, 6).tolist()


def block(matrix, rows, columns):
    if not matrix or len(matrix) == 0:
        return []
        
    arr = np.array(matrix, dtype=float)
    
    # Удаляем строки, если список индексов строк не пуст
    if len(rows) > 0:
        arr = np.delete(arr, rows, axis=0)
        
    # Удаляем столбцы, если список индексов столбцов не пуст
    if len(columns) > 0 and arr.size > 0:
        arr = np.delete(arr, columns, axis=1)
        
    return arr.tolist()


def column_means(matrix):
    if not matrix or len(matrix) == 0 or len(matrix)[0] == 0:
        return []
        
    arr = np.array(matrix, dtype=float)
    means = np.round(np.mean(arr, axis=0), 6)
    return means.tolist()


def column_range(matrix, index):
    if not matrix or len(matrix) == 0 or len(matrix)[0] == 0:
        return 0.0
        
    arr = np.array(matrix, dtype=float)
    column = arr[:, index]
    col_range = np.round(np.max(column) - np.min(column), 6)
    return float(col_range)
