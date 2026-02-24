import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    tokenized_docs = []
    vocabulary = set()
    
    for i, document in enumerate(documents):
        tokens = document.lower().split(" ")
        tokenized_docs.append(tokens)
        vocabulary.update(tokens)

    vocabulary = sorted(list(vocabulary))
    token_index = {term: idx for idx, term in enumerate(vocabulary)}

    N_docs = len(documents)
    N_vocab = len(vocabulary)
    tfidf_matrix = np.zeros((N_docs, N_vocab))

    df_count = Counter()
    for tokens in tokenized_docs:
        unique_tokens = set(tokens)
        for token in unique_tokens:
            df_count[token] += 1

    for i, tokens in enumerate(tokenized_docs):
        total_words = len(tokens)
        terms_count = Counter(tokens)
        for term, term_count in terms_count.items():
            tf = term_count / total_words

            idf = np.log(N_docs / df_count[term])

            tfidf = tf * idf

            tfidf_matrix[i][token_index[term]] = tfidf

    return (tfidf_matrix, vocabulary)