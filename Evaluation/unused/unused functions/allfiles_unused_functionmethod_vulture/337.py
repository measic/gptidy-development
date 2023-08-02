# 2 1d ODEs
def ode(state,t):
    # x and y are first two components of state vector
    x = state[0]

    # Compute state derivatives.  Mess around here! 
    dx = .4* np.square(x) - 2

    # Return the state derivatives
    return [dx]