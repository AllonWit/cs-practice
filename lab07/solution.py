import numpy as np

def column_means(matrix: list) -> list:
    if not matrix or not matrix[0]:
        return []
    
    arr = np.array(matrix, dtype=np.float64)
    means = np.mean(arr, axis=0)
    return np.round(means, 6).tolist()