import numpy as np

def column_means(matrix: list) -> list:
    if not matrix or not matrix[0]:
        return []
    
    arr = np.array(matrix, dtype=np.float64)
    means = np.mean(arr, axis=0)
    return np.round(means, 6).tolist()

def normalize_rows(matrix: list) -> list:
    if not matrix or not matrix[0]:
        return []
    
    arr = np.array(matrix, dtype=np.float64)
    row_min = np.min(arr, axis=1, keepdims=True)
    row_max = np.max(arr, axis=1, keepdims=True)
    
    row_range = row_max - row_min
    # Защита от деления на ноль для строк из одинаковых чисел
    row_range = np.where(row_range == 0, 1.0, row_range)
    
    normalized = (arr - row_min) / row_range
    return np.round(normalized, 6).tolist()