def discount_returns(rewards: list, gamma: float) -> list:
    """
    Returns the discounted return at every timestep.
    """
    # Write code here
    Gt = rewards[:]
    for i in range(len(rewards)-2, -1, -1):
        Gt[i] = Gt[i] + gamma*Gt[i+1]

    return Gt