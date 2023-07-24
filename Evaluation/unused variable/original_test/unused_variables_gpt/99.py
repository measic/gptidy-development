mu = Partition([2,1])
n = 3
v = vandermonde(mu)
deg_v = v.degree()
generator = {v.multidegree() : [v]}
list_op = partial_derivatives(v.parent())
W1 = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)

op_pol = polarization_operators(2, deg_v)
W2 = PolarizedSpace(IsotypicComponent(W1, n), op_pol)
show(character(W2))
for v in W2.values():
    show(v.basis())