from devito import norm
assert np.isclose(norm(image), 1e7, rtol=1e1)