mu = Partition([2,1,1])
n = 4
r = n-1
v = vandermonde(mu)
deg_v = v.degree()
generator = {v.multidegree() : [v]}
list_op = partial_derivatives(v.parent())
W1 = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)

op_pol = polarization_operators(r, max_deg=deg_v, row_symmetry="permutation")
W2 = PolarizedSpace(IsotypicComponent(W1, n), op_pol, add_degrees=add_degrees_symmetric)
show(character(W2, row_symmetry="permutation"))
for v in W2.values():
    show(v.basis())