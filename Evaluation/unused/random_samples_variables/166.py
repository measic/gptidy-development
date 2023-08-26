# incidence and screening based on 2014 data
cov_2014 = 493327. / 3500026.
adpc_2014 = 47437. / 3500026.
[incsol, scrsol] = fsolve(
    lambda x: [test_diag_fun(x)[0] - cov_2014, test_diag_fun(x)[1] - adpc_2014], 
    [0.09, 0.25] 
    )
inc = incsol
scr = scrsol
parms = \
    [incsol*p_asymp, sc + scrsol*p_true_pos, incsol*(1-p_asymp), scrsol*p_true_pos + att_symp*p_true_pos]

# solve, 2013-2014
sol_13_14 = odeint(dydt, 
       sol_12_13[999,:], 
       linspace(0,10,1000), 
       args = (parms,)
      )