def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if not tokens:
        return []
    N = len(tokens)
    chunk_list = []
    step = chunk_size - overlap
    for i in range(0, N, step):
        chunk_list.append(tokens[i:i+chunk_size])
        if(i + chunk_size >= N):
            break
    return chunk_list