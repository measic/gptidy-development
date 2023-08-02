def function_def(f, index):
    return np.moveaxis(f, index, 0).copy()