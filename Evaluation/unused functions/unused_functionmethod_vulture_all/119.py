def value_iteration(V_init, PI_init, P, R, states, actions, next_states, gamma, epsilon=1e-4):
    
    #1. INITIALIZATION
    V_k = copy.deepcopy(V_init)  # V(s) ... our value function estimate for PI
    PI = copy.deepcopy(PI_init)  # PI(s) ... our greedy policy
        
    # 2. POLICY EVALUATION (makes only 1 sweep before taking the max over the actions)
    k = 0
    V_kplus1 = copy.deepcopy(V_k)
    delta = epsilon + 1
    
    while delta > epsilon:

        delta = 0
        
        Q = {0: {0: 0,   # state0, action0
                 1: 0},  # state0, action1
             1: {2: 0}}  # state1, action2
        for s in states:
            v = 0
            for a in actions[s]:
                for n in next_states:
                
                    # Bellman's optimality update rule
                    Q[s][a] += P[n,s,a] * (R[s,a] + gamma * V_k[n])

            # This step replaces the poilicy improvement step (gets the maximal value)
            V_kplus1[s] = max(Q[s].items(), key=operator.itemgetter(1))[1]
            
            # Keeps biggest difference seen so far
            delta = np.max([delta, np.abs(V_kplus1[s] - V_k[s])])

        # Updates our current estimate
        V_k = copy.deepcopy(V_kplus1)
        k += 1
    
    # Updates the policy to be greedy with respect to the value function
    for s in states:
        PI[s] = max(Q[s].items(), key=operator.itemgetter(1))[0]
    
    return V_k, k, PI 