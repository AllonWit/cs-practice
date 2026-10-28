import numpy as np

def reshape_rows(values, width):
    if not values or width <= 0 or len(values) % width != 0:
        return []
    
    matrix = np.array(values, dtype=float).reshape(-1, width)
    return np.round(matrix, 6).tolist()


def block(matrix, rows, columns):
    if not matrix or not rows or not columns:
        return []
        
    arr = np.array(matrix, dtype=float)
    if arr.ndim == 1:
        arr = np.atleast_2d(arr)
        
    # Вырезаем подматрицу на пересечении указанных строк и столбцов
    res = arr[np.ix_(rows, columns)]
    return np.round(res, 6).tolist()


def column_means(matrix):
    if not matrix:
        return []
        
    arr = np.array(matrix, dtype=float)
    means = np.round(np.mean(arr, axis=0), 6)
    
    if means.ndim == 0:
        return [float(means)]
    return means.tolist()


def column_range(matrix, index):
    if not matrix:
        return 0.0
        
    arr = np.array(matrix, dtype=float)
    if arr.ndim == 1:
        return 0.0
        
    column = arr[:, index]
    col_range = np.round(np.max(column) - np.min(column), 6)
    return float(col_range)

