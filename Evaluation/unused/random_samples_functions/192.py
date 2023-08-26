def policy_iteration(V_init, PI_init, world_size, states, actions, nextState, gamma, epsilon=1e-4, modified=False):

    # The reward is always -1
    R = -1
    
    #1. INITIALIZATION
    V_k = copy.deepcopy(V_init)
    PI = copy.deepcopy(PI_init)
    policy_stable = False
    all_k = []
    idx_to_a = {0:'L', 1:'U', 2:'R', 3:'D'}

    while not policy_stable:
        
        # 2. POLICY EVALUATION (iterates until V_k converges)
        k = 0
        V_kplus1 = copy.deepcopy(V_k)
        delta = epsilon + 1
        
        while delta > epsilon and (k < 5 or not modified):

            delta = 0
            for i, j in states:
                
                # Here the next state is fully defined by the policy (there is no uncertainty on the transition)
                a = idx_to_a[PI[i,j]]
                newPosition = nextState[i][j][a]
                P = 1.

                # Bellman's update rule
                V_kplus1[i, j] = P * (R + gamma * V_k[newPosition[0], newPosition[1]])

                # Keeps biggest difference seen so far
                delta = np.max([delta, np.abs(V_kplus1[i,j] - V_k[i,j])])

            # Updates our current estimate
            V_k = copy.deepcopy(V_kplus1)
            k += 1
        all_k.append(k)

        # 3. POLICY IMPROVEMENT (greedy action selection with respect to V_k)
        Q = np.zeros((world_size, world_size, 4), dtype=np.float)
        
        policy_stable = True
        old_PI = copy.deepcopy(PI)
        
        for i, j in states:
            for a_idx in range(4): # actions
                    
                # Again the next state is fully defined by the chosen action (there is no uncertainty on the transition)
                a = idx_to_a[a_idx]
                newPosition = nextState[i][j][a]
                P = 1.

                # Policy Improvement rule
                Q[i,j,a_idx] = P * (R + gamma * V_k[newPosition[0], newPosition[1]])
                    
            PI[i,j] = np.argmax(Q[i,j,:])
                    
            if old_PI[i,j] != PI[i,j]:
                policy_stable = False
    
    return V_k, all_k, PI 