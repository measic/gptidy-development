# incidence and screening based on 2015 data
cov_2015 = 446279. / 3496125.
adpc_2015 = 44609. / 3496125.
[incsol, scrsol] = fsolve(
    lambda x: [test_diag_fun(x)[0] - cov_2015, test_diag_fun(x)[1] - adpc_2015], 
    [0.09, 0.25] 
    )
inc = incsol
scr = scrsol
parms = \
    [incsol*p_asymp, sc + scrsol*p_true_pos, incsol*(1-p_asymp), scrsol*p_true_pos + att_symp*p_true_pos]

# solve, 2013-2014
sol_14_15 = odeint(dydt, 
       sol_13_14[999,:], 
       linspace(0,10,1000), 
       args = (parms,)
      )