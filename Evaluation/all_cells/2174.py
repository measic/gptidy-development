def add_degrees_isotypic(gen_deg, op_deg):
    D = cartesian_product([ZZ for i in range(len(gen_deg[0]))])
    return D(gen_deg[0])+D(op_deg), gen_deg[1]

def add_degrees_symmetric(gen_deg,op_deg):
    D = cartesian_product([ZZ for i in range(len(gen_deg[0]))])
    d = D(gen_deg[0])+D(op_deg)
    return D(sorted(d, reverse=True)), gen_deg[1]

def add_degrees_test(gen_deg, op_deg):
    return gen_deg+op_deg