import torch

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Returns the scaled dot-product attention output.
    """
    d_k = K.shape[-1]
    inner_term = torch.matmul(Q, K.transpose(-1, -2)) / torch.sqrt(torch.tensor(d_k))
    term = torch.matmul(torch.nn.functional.softmax(inner_term, dim=-1), V)
    return term