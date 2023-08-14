def policy_iteration(V_init, PI_init, P, R, states, actions, next_states, gamma, epsilon=1e-4, modified=False):
    
    #1. INITIALIZATION
    V_k = copy.deepcopy(V_init)  # V(s) ... our value function estimate for PI
    PI = copy.deepcopy(PI_init)  # PI(s) ... our greedy policy
    policy_stable = False
    all_k = []
    
    while not policy_stable:
        
        # 2. POLICY EVALUATION (iterates until V_k converges) 
        k = 0
        V_kplus1 = copy.deepcopy(V_k)
        delta = epsilon + 1
        while delta > epsilon and (k < 5 or not modified):

            delta = 0
            for s in states:
                v = 0
                for n in next_states:

                    # Bellman's update rule
                    a = int(PI[s])
                    v += P[n,s,a] * (R[s,a] + gamma * V_k[n])

                # Keeps biggest difference seen so far
                V_kplus1[s] = v
                delta = np.max([delta, np.abs(V_kplus1[s] - V_k[s])])

            # Updates our current estimate
            V_k = copy.deepcopy(V_kplus1)
            k += 1
        all_k.append(k)

        # 3. POLICY IMPROVEMENT (greedy action selection with respect to V_k)
        Q = {0: {0: 0,   # state0, action0
                 1: 0},  # state0, action1
             1: {2: 0}}  # state1, action2
        
        policy_stable = True
        old_PI = copy.deepcopy(PI)
        
        for s in states: 
            for a in actions[s]:
                for n in next_states:
                    
                    # Policy Improvement rule
                    Q[s][a] += P[n,s,a] * (R[s,a] + gamma * V_k[n])
                    
            PI[s] = max(Q[s].items(), key=operator.itemgetter(1))[0]
                    
            if old_PI[s] != PI[s]:
                policy_stable = False
    
    return V_k, all_k, PI 