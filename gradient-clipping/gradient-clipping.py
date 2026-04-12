import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.array(g)
    if max_norm <= 0: return g
    
    g_clipped = np.linalg.norm(g)

    if g_clipped > max_norm:
        g = g * (max_norm/g_clipped)

    return g