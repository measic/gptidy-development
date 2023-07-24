# North Lincolnshire
# find steady state based on 2012 data

cov_2012 = 0.100807801953
adpc_2012 = 0.0111652211547
[incsol, scrsol] = fsolve(
    lambda x: [test_diag_fun(x)[0] - cov_2012, test_diag_fun(x)[1] - adpc_2012],
    [0.09, 0.25]
)

U_2012 = U_fun(
    incsol * p_asymp, sc + scrsol * p_true_pos, incsol * (1 - p_asymp), scrsol * p_true_pos + att_symp * p_true_pos
)
A_2012 = A_fun(
    incsol * p_asymp, sc + scrsol * p_true_pos, incsol * (1 - p_asymp), scrsol * p_true_pos + att_symp * p_true_pos
)
S_2012 = S_fun(
    incsol * p_asymp, sc + scrsol * p_true_pos, incsol * (1 - p_asymp), scrsol * p_true_pos + att_symp * p_true_pos
)


# find incidence and screening based on 2013 data
cov_2013 = 0.173269822929
adpc_2013 = 0.0216211803756
[incsol, scrsol] = fsolve(
    lambda x: [test_diag_fun(x)[0] - cov_2013, test_diag_fun(x)[1] - adpc_2013],
    [0.09, 0.25]
)

# solve, 2012-2013
inc = incsol
scr = scrsol
parms = [
    incsol * p_asymp, sc + scrsol * p_true_pos, incsol * (1 - p_asymp), scrsol * p_true_pos + att_symp * p_true_pos
]

sol_n_lincs = odeint(dydt,
                     [U_2012, A_2012, S_2012],
                     linspace(0, 10, 1000),
                     args=(parms,)
                     )