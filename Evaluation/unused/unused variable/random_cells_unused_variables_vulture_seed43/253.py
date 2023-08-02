def character(S, left_basis=s, right_basis=s, row_symmetry=None):
    if isinstance(S, dict):
        return sum(character(V,
                             left_basis=left_basis, right_basis=right_basis, row_symmetry=row_symmetry) 
                   for V in S.values())
    else:
        basis = S.basis()
        basis_element = basis.values().pop()[0]
        P = basis_element.parent()
        n = P.ncols()
        r = P.nrows()
        
        charac = 0
        if row_symmetry != "permutation":
            q = PolynomialRing(QQ,'q',r).gens()

        for nu in Partitions(n):
            basis_nu = {}
            charac_nu = 0
            # Get the nu_isotypic part of the basis
            for key, value in basis.iteritems():
                if Partition(key[1]) == nu:
                    basis_nu[key[0]] = value

            # Use monomials to compute the character
            if row_symmetry == "permutation":
                for deg, b in basis_nu.iteritems():
                    charac_nu += sum(m(Partition(deg)) for p in b)
                if charac_nu != 0 :
                    if left_basis == s :
                        charac_nu = s(charac_nu).restrict_partition_lengths(r,exact=False)
                    elif left_basis != m :
                        charac_nu = left_basis(charac_nu)

            # Or use directly the degrees
            else:
                for deg, b in basis_nu.iteritems():
                    charac_nu += sum(prod(q[i]**deg[i] for i in range(0,len(deg))) for p in b)
                if charac_nu != 0 :
                    if left_basis == s :
                        charac_nu = s.from_polynomial(charac_nu).restrict_partition_lengths(r,exact=False)           
                    else:
                        charac_nu = left_basis.from_polynomial(charac_nu)

            # Make the tensor product with s[nu]
            if charac_nu != 0:
                charac += tensor([charac_nu, right_basis(s(nu))])
        return charac