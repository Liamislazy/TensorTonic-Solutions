import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p = np.array(p)
    y = np.array(y)
    if p.ndim == 2:
        p_new = p.flatten()
        y_new = y.flatten()
        
        return 1 - ((2*(np.dot(p_new, y_new)) + eps)/(np.sum(p_new) + np.sum(y_new) + eps))
    else:
        return 1 - ((2*(np.dot(p, y)) + eps)/(np.sum(p) + np.sum(y) + eps))
    