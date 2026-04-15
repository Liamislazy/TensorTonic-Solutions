def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    if len(list(set(set_a) | set(set_b))) == 0: return 0;
    return len(list(set(set_a) & set(set_b))) / len(list(set(set_a) | set(set_b)))