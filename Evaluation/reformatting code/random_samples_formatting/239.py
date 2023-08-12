def partial_derivatives(P):
    """
    Return the partial derivative functions in all the variables of `P`.
    
    INPUT:
    - `P` -- a diagonal polynomial ring
    
    """
    n = P.ncols()
    r = P.nrows()
    D = P.grading_set()
    X = P.derivative_variables()
    op = {}
    for i in range(r):
        op[D((-1 if j==i else 0 for j in range(r)))] = [attrcall("derivative", X[i,k]) for k in range(n)]
    return op

def polarization_operators(r, max_deg=1, side=None, row_symmetry=None):
    D = cartesian_product([ZZ for i in range(r)])
    return {D([-d if i==i1 else 1 if i==i2 else 0 for i in range(r)]):
            [attrcall("polarization", i1=i1, i2=i2, d=d, row_symmetry=row_symmetry)]
            for d in range(1, max_deg+1)
            for i1 in range(0, r)
            for i2 in range(0, r)
            if (i1<i2 if side == 'down' else i1!=i2)
           }

##############################################################

def steenrod_operators(r, degree=1, row_symmetry=None):
    D = cartesian_product([ZZ for i in range(r)])
    op = {}
    for i in range(r):
        op[D((-degree if j==i else 0 for j in range(r)))] = [
            attrcall("steenrod_op", i=i, k=degree+1, row_symmetry=row_symmetry)]
    return op

def diagonal_steenrod_operators(list_deg):
    r = len(list_deg[0])
    D = cartesian_product([ZZ for i in range(r)])
    op = {}
    for dx, dy in list_deg:
        op[D((-dx if j==0 else -dy if j==1 else 0 for j in range(r)))] = [
            attrcall("diagonal_steenrod", i1=0, i2=1, d1=dx, d2=dy)]
    return op

def higher_polarization_operators(r, max_deg=1, side=None, row_symmetry=None):
    D = cartesian_product([ZZ for i in range(r)])
    return {D([-d1 if i==i1 else d2 if i==i2 else 0 for i in range(r)]):
            [attrcall("higher_polarization", i1=i1, i2=i2, d1=d1, d2=d2, row_symmetry=row_symmetry)]
            for d1 in range(1, max_deg+1)
            for d2 in range(1, 3)
            for i1 in range(0, r)
            for i2 in range(0, r)
            if (i1<i2 if side == 'down' else i1!=i2)
           }

def multipolarization(list_deg, i2):
    r = len(list_deg[0])
    D = cartesian_product([ZZ for i in range(r)])
    return {D(-d[i]+1 if i==i2 else -d[i] for i in range(len(d))) : 
            [attrcall("multi_polarization", D=d, i2=i2)] for d in list_deg}

def symmetric_derivatives(list_deg, row_symmetry=None):
    r = len(list_deg[0])
    D = cartesian_product([ZZ for i in range(r)])
    return {D(-i for i in d) : [attrcall("symmetric_derivative", d=d, row_symmetry=row_symmetry)] 
            for d in list_deg}