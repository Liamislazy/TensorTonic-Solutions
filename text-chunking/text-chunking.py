def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if tokens == []:
        return []
    N = len(tokens)
    chunk_list = []
    step = chunk_size - overlap
    i = 0
    while i + chunk_size < N:
        chunk_list.append(tokens[i:i+chunk_size])
        i += step

    chunk_list.append(tokens[i:])
    return chunk_list