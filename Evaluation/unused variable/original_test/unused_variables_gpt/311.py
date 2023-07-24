def vandermonde(gamma, r=0):
    n = gamma.size()
    if r == 0:
        r = 1
    P = DiagonalPolynomialRing(QQ, n, r, inert=1) 
    X = P.variables()
    Theta = P.inert_variables()
    return matrix([[x**i[1]*theta**i[0] for i in gamma.cells()] 
                   for x,theta in zip(X[0],Theta[0])]).determinant()