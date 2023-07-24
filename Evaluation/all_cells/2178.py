def Range(S, operators, add_degrees=add_degrees_isotypic):
    if isinstance(S, dict):
        return {key : Range(value, operators, add_degrees=add_degrees)
                for key, value in S.iteritems()}

    result = {}
    basis = S.basis()
    for key, b in basis.iteritems():
        result = merge(result, {add_degrees(key, deg): 
                                     [op(p) for p in b for op in op_list if op(p)!=0] 
                                     for deg, op_list in operators.iteritems()})    
    if result != {} :
        return Subspace(result, {}, add_degrees) #{} <-> operators
    else :
        return None