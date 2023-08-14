v = vandermonde(Diagram([(0,0),(1,0),(2,0),(3,0),(0,1),(2,1)]))
deg_v = v.degree()
generator = {v.multidegree() : [v]}
list_op = partial_derivatives(v.parent())
W1 = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)

op_pol = polarization_operators(3, max_deg=deg_v, row_symmetry="permutation")
#W2 = PolarizedSpace(IsotypicComponent(W1, 6, use_antisymmetry=True), op_pol)
#character(W2, row_symmetry="permutation")