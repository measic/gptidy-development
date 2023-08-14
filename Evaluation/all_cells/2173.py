def IsotypicComponent(S, arg, use_antisymmetry=False):
    if isinstance(arg, Partition):
        list_partitions = [arg]
    elif isinstance(arg, Integer):
        list_partitions = Partitions(arg)
    else : 
        print("Error: arg should be a partition or an integer.")
    
    basis = S.basis()
    result = {}
    P1 = basis.values().pop()[0].parent()
    for nu in list_partitions:
        result_nu = {}
        if use_antisymmetry == True:
            antisymmetries = antisymmetries_of_tableau(nu.initial_tableau())
            P2 = DiagonalAntisymmetricPolynomialRing(P1._R, P1.ncols(), P1.nrows(), 
                                                 P1.ninert(), antisymmetries)
        for deg, value in basis.iteritems():
            if use_antisymmetry:
                gen = []
                for p in value:
                    temp = apply_young_idempotent(P2(p), nu)
                    if temp != 0: 
                        gen += [temp]
            else:
                gen = []
                for p in value:
                    temp = apply_young_idempotent(p, nu)
                    if temp != 0:
                        gen += [temp]
            if gen != []:
                result_nu[(deg, tuple(nu))] = Subspace(gen, {}).basis()[0]
        if result_nu != {}:
            result[nu] = Subspace(result_nu, operators={})
                
    if len(result.keys()) == 1:
        key = result.keys()[0]
        return result[key]
    else:
        return result