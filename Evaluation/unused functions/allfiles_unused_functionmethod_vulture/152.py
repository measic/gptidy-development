def compute_character(mu, use_antisymmetry=True, row_symmetry="permutation"):
    n = Integer(mu.size())
    # Determinant computation
    v = vandermonde(mu)
    # Span by derivatives
    generator = {v.multidegree() : [v]}
    list_op = partial_derivatives(v.parent())
    V = Subspace(generators=generator, operators=list_op, add_degrees=add_degree)
    # Projection on isotypic components
    V_iso = IsotypicComponent(V, n, use_antisymmetry=use_antisymmetry)
    # Polarization
    r = n-1
    deg = v.degree()
    if deg == 0:
        deg = 1
    op_pol = polarization_operators(r, deg, row_symmetry=row_symmetry)
    V_pol = PolarizedSpace(V_iso, op_pol)
    
    # character
    return character(V_pol, row_symmetry=row_symmetry)