t1 = datetime.datetime.now()
mu = Partition([3,1])
n = mu.size()
r = n-1
v = vandermonde(mu)
deg_v = v.degree()
generator = {v.multidegree() : [v]}
list_op = partial_derivatives(v.parent())
W1 = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)

op_pol = polarization_operators(r, deg_v)
W2 = PolarizedSpace(IsotypicComponent(W1, n, use_antisymmetry=True), op_pol)
show(character(W2))
t2 = datetime.datetime.now()
show(t2-t1)