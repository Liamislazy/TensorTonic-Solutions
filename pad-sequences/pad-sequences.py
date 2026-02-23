import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    N = len(seqs)
    if N == 0:
        return np.empty(0, max_len if max_len is not None else 0)
    # find max len
    if max_len == None:
        max_len = max((len(seq) for seq in seqs), default=0)
        
    seqs_numpy = np.full((N, max_len), pad_value)
    
    for i, seq in enumerate(seqs):
        trunc_size = min(max_len, len(seq))

        seqs_numpy[i, :trunc_size] = seq[:trunc_size]
    
    return seqs_numpy