# Initializations
V_init = np.zeros((2,), dtype=np.float)                            # V(s) ... our value function estimate for PI
PI_init = np.array([np.random.uniform(0, 2), 2], dtype=np.int)     # PI(s) ... our greedy policy

# The 2-states world
P, R, states, actions, next_states, gamma = create_2statesworld()

print("INITIALIZATION")
print("Initial value function V is filled with zeros whereas initial policy is random among legal actions for each state")
print("\nV = ", np.round(V_init))
print("\nPI = ", PI_init)


PolIt_results = policy_iteration(V_init, PI_init, P, R, states, actions, next_states, gamma)

print("\n\nRESULTS FOR POLICY ITERATION -------------")
print("Policy found in {} iterations, where each policy evaluation lasted for k = {}".format(len(PolIt_results[1]), PolIt_results[1]))
print("\nV = ", np.round(PolIt_results[0], 2))
print("\nPI = ", PolIt_results[2])

ValIt_results = value_iteration(V_init, PI_init, P, R, states, actions, next_states, gamma)

print("\n\nRESULTS FOR VALUE ITERATION -------------")
print("Policy found in {} iterations".format(ValIt_results[1]))
print("\nV = \n", np.round(ValIt_results[0], 2))
print("\nPI = ", ValIt_results[2])


M_PolIt_results = policy_iteration(V_init, PI_init, P, R, states, actions, next_states, gamma, modified=True)

print("\n\nRESULTS FOR MODIFIED POLICY ITERATION -------------")
print("Policy found in {} iterations, where each policy evaluation lasted for k = {}".format(len(M_PolIt_results[1]), M_PolIt_results[1]))
print("\nV = ", np.round(M_PolIt_results[0], 2))
print("\nPI = ", M_PolIt_results[2])

print("\n\nEFFECT OF GAMMA ON CONVERGENCE SPEED")

logg = {"policy_iteration": [], "value_iteration": [], "M_policy_iteration": []}
# For different values of gamma
gammas = [0.50, 0.75, 0.90, 0.95]
for g in gammas:
    
    # Run Policy Iteration
    _, PolIt_k, _ = policy_iteration(V_init, PI_init, P, R, states, actions, next_states, g)
    logg['policy_iteration'].append(sum(PolIt_k))
    
    # Run Value Iteration
    _, ValIt_k, _ = value_iteration(V_init, PI_init, P, R, states, actions, next_states, g)
    logg['value_iteration'].append(ValIt_k)
    
    # Run Modified Policy Iteration
    _, M_PolIt_k, _ = policy_iteration(V_init, PI_init, P, R, states, actions, next_states, g, modified=True)
    logg['M_policy_iteration'].append(sum(M_PolIt_k))
    
plt.figure(figsize=(10,4))
plt.plot(gammas, logg['policy_iteration'], label="Policy Iteration")
plt.plot(gammas, logg['value_iteration'], label="Value Iteration")
plt.plot(gammas, logg['M_policy_iteration'], label="Modified Policy Iteration")
plt.title('Effect of gamma on convergence speed', fontweight='bold')
plt.xlabel('Gamma')
plt.ylabel('Number of full prediction sweeps')
plt.legend(loc='best')
plt.show()