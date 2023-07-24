def move_dimension_first(f, index):
    return np.moveaxis(f, index, 0).copy()
