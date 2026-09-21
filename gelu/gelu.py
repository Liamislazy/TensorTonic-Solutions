import math
import numpy as np

_erf_vectorized = np.vectorize(math.erf)
def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    x = np.asarray(x, dtype=np.float64)
    return 0.5 * x * (1.0 + _erf_vectorized(x / np.sqrt(2.0)))

    
    