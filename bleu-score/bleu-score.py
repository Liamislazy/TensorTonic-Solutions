from collections import Counter
import math

def get_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """ 
    bleu = 0
    eps = 1e-6
    n_candidate = len(candidate)
    n_reference = len(reference)

    if n_candidate == 0:
        return 0.0
    
    for i in range(1, max_n+1):
        candidate_ngrams = get_ngrams(candidate, i)
        reference_ngrams = get_ngrams(reference, i)
        
        candidate_count = Counter(candidate_ngrams)
        reference_count = Counter(reference_ngrams)
        
        clipped_sum = sum(min(candidate_count[n_gram_term], reference_count[n_gram_term]) for n_gram_term in candidate_count)
        sum_candidate = sum(candidate_count.values())
        
        if sum_candidate == 0:
            p = 0
        else:
            p = clipped_sum / sum_candidate
        
        bleu += math.log(p)
    
    if n_candidate >= n_reference:
        bp = 1.0
    else:
        bp = math.exp(1 - (n_reference / n_candidate))
    final_bleu = bp * math.exp((bleu / max_n))
    return final_bleu