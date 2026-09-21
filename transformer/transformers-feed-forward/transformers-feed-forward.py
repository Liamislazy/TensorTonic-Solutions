import numpy as np

def ReLU(X):
    return np.maximum(0, X)

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Returns the position-wise feed-forward output.
    """
    return ReLU(x@W1 + b1)@W2 + b2