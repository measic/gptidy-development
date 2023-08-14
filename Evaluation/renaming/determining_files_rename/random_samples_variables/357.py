variable_def, _, _, f = window_bounds(((x_start, 5000), (y_start, 5000)), orig_aff)
a, b, _, d, e, _, _, _, _ = tuple(orig_aff)
new_aff = rasterio.Affine(a, b, variable_def, d, e, f)