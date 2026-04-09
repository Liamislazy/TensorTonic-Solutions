import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    
    return np.array([i if i > 0 else i * alpha for i in x])