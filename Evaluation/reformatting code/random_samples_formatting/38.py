v = vandermonde(Partition([3,1,1]))
deg_v = v.degree()
generator = {v.multidegree() : [v]}
list_op = partial_derivatives(v.parent())
W1 = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)

op_pol = polarization_operators(2, max_deg=deg_v)
W2 = PolarizedSpace(IsotypicComponent(W1, 5), op_pol)
character(W2)