def create_2statesworld():

    P = np.zeros((2,2,3)) # P(s'|s,a) ... our model of the environment
    P[0,0,0] = 0.5
    P[1,0,0] = 0.5
    P[1,0,1] = 1.
    P[1,1,2] = 1.

    R = np.zeros((2,3))  # R(s,a) ... the reward funciton 
    R[0,0] = 5
    R[0,1] = 10
    R[1,2] = -1

    states = [0, 1]
    actions = [[0, 1], [2]]
    next_states = [0, 1]
    gamma = 0.95
    
    return P, R, states, actions, next_states, gamma