def f(gamma):
    v = vandermonde(gamma)
    n = gamma.size()
    deg_v = v.degree()
    generator = {v.multidegree() : [v]}
    list_op = partial_derivatives(v.parent())
    W1 = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)

    r = 1
    op_pol = polarization_operators(r, deg_v, row_symmetry="permutation")
    show(IsotypicComponent(W1, Partition([1 for i in range(n)])).basis())
    show(IsotypicComponent(W1, gamma).basis())
    W1 = PolarizedSpace(IsotypicComponent(W1, n, use_antisymmetry=True), op_pol)
    return character(W1, row_symmetry="permutation")