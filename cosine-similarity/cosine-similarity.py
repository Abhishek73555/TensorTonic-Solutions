import numpy as np

def cosine_similarity(x, y):
    if len(x) != len(y):
        raise ValueError("Vectors must have same length")

    dot = 0
    for i in range(len(x)):
        dot += x[i] * y[i]

    norm_x = np.sqrt(sum(x[i] * x[i] for i in range(len(x))))
    norm_y = np.sqrt(sum(y[i] * y[i] for i in range(len(y))))

    if norm_x == 0 or norm_y == 0:
        return 0.0

    return float(dot / (norm_x * norm_y))