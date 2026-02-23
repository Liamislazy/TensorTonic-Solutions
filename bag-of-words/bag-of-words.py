import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    bow_array = []
    tokens_dict = {}
    for token in tokens:
        tokens_dict[token] = 0
    
    for token in tokens:
        tokens_dict[token] += 1
    
    for word in vocab:
        if word in tokens:
            bow_array.append(tokens_dict[word])
        else:
            bow_array.append(0)
    bow_array_numpy = np.array(bow_array, dtype=int)
    return bow_array_numpy