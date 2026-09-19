import numpy as np


def calculate(list_input):
    # Check if the input list contains exactly 9 numbers
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3x3 NumPy array
    matrix = np.array(list_input).reshape(3, 3)

    # Calculate required statistics for axis=0 (columns), axis=1 (rows), and flattened matrix
    calculations = {
        "mean": [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist(),
        ],
        "variance": [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist(),
        ],
        "standard deviation": [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist(),
        ],
        "max": [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist(),
        ],
        "min": [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist(),
        ],
        "sum": [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist(),
        ],
    }

    return calculations