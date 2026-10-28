import numpy as np

def reshape_means(values, width):
    if not values or width <= 0 or len(values) % width != 0:
        return []
    
    # Преобразуем в двумерную матрицу заданной ширины
    matrix = np.array(values, dtype=float).reshape(-1, width)
    
    # Вычисляем среднее по строкам и округляем до 6 знаков
    means = np.round(np.mean(matrix, axis=1), 6)
    return means.tolist()


def blank(matrix, rows, columns):
    if not matrix or len(matrix) == 0:
        return []
        
    arr = np.array(matrix, dtype=float)
    
    # Удаляем указанные строки и столбцы
    arr = np.delete(arr, rows, axis=0)
    arr = np.delete(arr, columns, axis=1)
    return arr.tolist()


def column_means(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return []
        
    arr = np.array(matrix, dtype=float)
    
    # Вычисляем среднее по столбцам и округляем до 6 знаков
    means = np.round(np.mean(arr, axis=0), 6)
    return means.tolist()


def column_range(matrix, index):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0.0
        
    arr = np.array(matrix, dtype=float)
    column = arr[:, index]
    
    # Разность между max и min в столбце с округлением до 6 знаков
    col_range = np.round(np.max(column) - np.min(column), 6)
    return float(col_range)
