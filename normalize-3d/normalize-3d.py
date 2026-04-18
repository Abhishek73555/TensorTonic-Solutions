import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) row-wise.
    Returns numpy array.
    """
    v = np.array(v, dtype=float)

    if v.ndim == 1:
        # Single vector
        norm = np.linalg.norm(v)
        return v if norm == 0 else v / norm

    elif v.ndim == 2:
        # Batch of vectors
        norms = np.linalg.norm(v, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1, norms)
        return v / norms

    else:
        raise ValueError("Input must be (3,) or (N,3)")