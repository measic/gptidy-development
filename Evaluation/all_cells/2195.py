mu = Partition([4,1])
n = mu.size()
v = vandermonde(mu)
generator = {v.multidegree() : [v]}
list_op = partial_derivatives(v.parent())
V = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)
V_iso = IsotypicComponent(V, n, use_antisymmetry=True)

r = n-1
deg = v.degree()
if deg == 0:
    deg = 1
op_pol = polarization_operators(r, deg, row_symmetry="permutation")
V_pol = PolarizedSpace(V_iso, op_pol)

character(V_pol, row_symmetry="permutation")