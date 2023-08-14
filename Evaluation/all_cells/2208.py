for nu in Partitions(3):
    print nu
    show(vandermonde(nu))
    show(antisymmetries_of_tableau(nu.initial_tableau()))