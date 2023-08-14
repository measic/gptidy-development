# Hyper-params
gamma = 0.95
epsilon = 1e-4

# The GRIDWORLD
world_size = 5
terminal_states = [(0,0), (world_size-1, world_size-1), (world_size-2, world_size-3), (2, world_size-int(world_size/2))]
actions, states, nextState = create_gridworld(world_size, terminal_states)

# Initializations
V_init = np.zeros((world_size, world_size), dtype=np.float)    # V(s) ... our value function estimate for PI
PI_init = np.random.randint(low=0, high=4, size=(world_size, world_size), dtype=np.int)     # PI(s) ... our greedy policy

print("INITIALIZATION")
print("Initial value function V is filled with zeros whereas initial policy is random")
print("\nV = \n", np.round(V_init))
print("\nPI = ")
print_policy(PI_init, terminal_states)

PolIt_results = policy_iteration(V_init, PI_init, world_size, states, actions, nextState, gamma, epsilon)

print("\n\nRESULTS FOR POLICY ITERATION -------------")
print("Policy found in {} iterations, where each policy evaluation lasted for k = {}".format(len(PolIt_results[1]), PolIt_results[1]))
print("\nV = \n", np.round(PolIt_results[0]))
print("\nPI = ")
print_policy(PolIt_results[2], terminal_states)

ValIt_results = value_iteration(V_init, PI_init, world_size, states, actions, nextState, gamma, epsilon)

print("\n\nRESULTS FOR VALUE ITERATION -------------")
print("Policy found in {} iterations".format(ValIt_results[1]))
print("\nV = \n", np.round(ValIt_results[0]))
print("\nPI = ")
print_policy(ValIt_results[2], terminal_states)

M_PolIt_results = policy_iteration(V_init, PI_init, world_size, states, actions, nextState, gamma, epsilon, modified=True)

print("\n\nRESULTS FOR MODIFIED POLICY ITERATION -------------")
print("Policy found in {} iterations, where each policy evaluation lasted for k = {}".format(len(M_PolIt_results[1]), M_PolIt_results[1]))
print("\nV = \n", np.round(M_PolIt_results[0]))
print("\nPI = ")
print_policy(M_PolIt_results[2], terminal_states)

print("\n\nEFFECT OF GAMMA ON CONVERGENCE SPEED")

logg = {"policy_iteration": [], "value_iteration": [], "M_policy_iteration": []}
# For different values of gamma
gammas = [0.50, 0.75, 0.90, 0.95]
for g in gammas:
    
    # Run Policy Iteration
    _, PolIt_k, _ = policy_iteration(V_init, PI_init, world_size, states, actions, nextState, g, epsilon)
    logg['policy_iteration'].append(sum(PolIt_k))
    
    # Run Value Iteration
    _, ValIt_k, _ = value_iteration(V_init, PI_init, world_size, states, actions, nextState, g, epsilon)
    logg['value_iteration'].append(ValIt_k)
    
    # Run Modified Policy Iteration
    _, M_PolIt_k, _ = policy_iteration(V_init, PI_init, world_size, states, actions, nextState, g, epsilon, modified=True)
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