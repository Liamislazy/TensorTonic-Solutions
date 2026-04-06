def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for step in range(steps):
        x = x0 - lr * (2*a*x0 + b)
        x0 = x

    return x0