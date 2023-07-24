ic = [1] # Initial condition
times = np.arange(0, 10, .1) # Times
orbit = odeint(ode, ic, times)
orbit2 = odeint(ode, [-10], times) # a second orbit