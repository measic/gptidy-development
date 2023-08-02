def function_def(X, name='Dataset'):
    """Print dataset size and dimensionality"""
    print('{}:\n  size: N={:,} x n={} -> {:,} floats\n  dim: {:,} features per clip\n  shape: {}'.format(name, np.prod(X.shape[:-1]), X.shape[-1], np.prod(X.shape), np.prod(X.shape[2:]), X.shape))