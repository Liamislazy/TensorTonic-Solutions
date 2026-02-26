import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    pos = np.arange(seq_len)[:, np.newaxis]

    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(base) / d_model))

    output = np.zeros((seq_len, d_model))

    output[:,0::2] = np.sin(pos * div_term)
    output[:,1::2] = np.cos(pos * div_term[:d_model // 2])
    
    return output
    