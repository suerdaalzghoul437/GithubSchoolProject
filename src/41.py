import numpy as np

def square_root(n):
    if n >= 0:
        return np.sqrt(n)
    else:
        raise ValueError("Input must be non-negative")

try:
    result = square_root(16)
    print(result)
except ValueError as e:
    print(e)
