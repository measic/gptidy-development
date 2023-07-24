prod = lambda x: reduce(mul, x)

def get_f(x, params, backend, lnK):
    init_concs = params[:n]
    eq_constants = params[n:]
    le = linear_exprs(preserv, x, linear_exprs(preserv, init_concs), rref=True)
    if lnK:
        return le + [
            sum(backend.log(xi)*p for xi, p in zip(x, coeffs)) - backend.log(K) 
            for coeffs, K in zip(stoichs, eq_constants)
        ]
    else:
        return le + [
            prod(xi**p for xi, p in zip(x, coeffs)) - K for coeffs, K in zip(stoichs, eq_constants)
        ]