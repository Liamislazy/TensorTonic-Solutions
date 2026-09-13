import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Returns the sinusoidal position matrix.
    """
    pos_arr = np.arange(seq_length)[:, np.newaxis]

    div_term = 1 / (10000 ** (np.arange(0, d_model, 2) / d_model))

    pos_seq = np.zeros((seq_length, d_model))

    pos_seq[:, 0::2] = np.sin(pos_arr * div_term)
    pos_seq[:, 1::2] = np.cos(pos_arr * div_term)
    
    return pos_seq
    