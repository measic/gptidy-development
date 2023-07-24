def character_quotient(M, N, n, r, left_basis=s, right_basis=s): # a corriger
    b_tot = M.basis()
    b_ideal = N.basis()
    charac = 0
    q = PolynomialRing(QQ,'q',r).gens()
    
    for nu in Partitions(n):
        basis_nu_tot = {}
        basis_nu_ideal = {}
        charac_nu = 0
        # Get the nu_isotypic part of the bases
        for key, value in b_tot.iteritems():
            if Partition(key[1]) == nu:
                basis_nu_tot[key[0]] = value
        for key, value in b_ideal.iteritems():
            if Partition(key[1]) == nu:
                basis_nu_ideal[key[0]] = value
                
        # Use the degrees to compute the character
        for deg, b in basis_nu_tot.iteritems():
            charac_nu += sum(prod(q[i]**deg[i] for i in range(0,len(deg))) for p in b)
        for deg, b in basis_nu_ideal.iteritems():
            charac_nu -= sum(prod(q[i]**deg[i] for i in range(0,len(deg))) for p in b)
        if charac_nu != 0 :
            if left_basis == s :
                charac_nu = s.from_polynomial(charac_nu).restrict_partition_lengths(r,exact=False)           
            else:
                charac_nu = left_basis.from_polynomial(charac_nu)      
            # Make the tensor product with s[nu]
            charac += tensor([charac_nu, right_basis(s(nu))])
            
    return charac