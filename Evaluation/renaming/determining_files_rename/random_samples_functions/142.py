def function_def(window, affine):
    (row_start, row_stop), (col_start, col_stop) = window
    w, s = (col_start, row_stop) * affine
    e, n = (col_stop, row_start) * affine
    return (w, s, e, n)