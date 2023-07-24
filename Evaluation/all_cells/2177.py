def PolarizedSpace(S, operators, add_degrees=add_degrees_isotypic):
    if isinstance(S, dict):
        return {key : PolarizedSpace(value, operators, add_degrees=add_degrees)
                for key, value in S.iteritems()}
    else:
        basis = S.basis()
        basis_element = basis.values().pop()[0]
        P1 = basis_element.parent()
        r = len(op_pol.keys().pop())
        row_symmetry = op_pol.values().pop()[0].kwds['row_symmetry']
        if row_symmetry == "permutation":
            add_degrees = add_degrees_symmetric
        D = cartesian_product([ZZ for i in range(r)])
        generators = {}

        if isinstance(P1, DiagonalAntisymmetricPolynomialRing):
            P2 = DiagonalAntisymmetricPolynomialRing(P1._R, P1.ncols(), r , P1.ninert(), P1.antisymmetries())
            for key, value in basis.iteritems():
                d = (D((key[0][0] if i==0 else 0 for i in range(0,r))), key[1])
                generators[d] = tuple(reduce_antisymmetric_normal(P2(b), 
                                                      b.parent().ncols(), 
                                                      b.parent().nrows()+b.parent().ninert(), 
                                                      b.antisymmetries()) for b in value)
        else :
            P2 = DiagonalPolynomialRing(P1._R, P1.ncols(), r , P1.ninert())
            for key, value in basis.iteritems():
                d = (D((key[0][0] if i==0 else 0 for i in range(0,r))), key[1])
                generators[d] = tuple(P2(b) for b in value)
        return Subspace(generators, operators, add_degrees=add_degrees)