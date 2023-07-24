def value_iteration(V_init, PI_init, world_size, states, actions, nextState, gamma, epsilon=1e-4):

    # The reward is always -1
    R = -1
    
    #1. INITIALIZATION
    V_k = copy.deepcopy(V_init)
    PI = copy.deepcopy(PI_init)
    idx_to_a = {0:'L', 1:'U', 2:'R', 3:'D'}
        
    # 2. POLICY EVALUATION (makes only 1 sweep before taking the max over the actions)
    k = 0
    V_kplus1 = copy.deepcopy(V_k)
    delta = epsilon + 1
    Q = np.zeros((world_size, world_size, 4), dtype=np.float)
    while delta > epsilon:

        # Only one sweep of evaluation before taking the max
        delta = 0
        for i, j in states:
            # Now evaluates the value function for each state for every possible action (not just with respect to current policy)
            for a_idx in range(4): # actions

                # Again the next state is fully defined by the chosen action (there is no uncertainty on the transition)
                a = idx_to_a[a_idx]
                newPosition = nextState[i][j][a]
                P = 1.

                # Update rule
                Q[i,j,a_idx] = P * (R + gamma * V_k[newPosition[0], newPosition[1]])

            # This step replaces the poilicy improvement step
            V_kplus1[i,j] = np.max(Q[i,j,:])

            # Keeps biggest difference seen so far
            delta = np.max([delta, np.abs(V_kplus1[i,j] - V_k[i,j])])

        # Updates our current estimate
        V_k = copy.deepcopy(V_kplus1)
        k += 1
        
    # Updates the policy to be greedy with respect to the value function
    for i, j in states:
        PI[i,j] = np.argmax(Q[i,j,:])
    
    return V_k, k, PI 