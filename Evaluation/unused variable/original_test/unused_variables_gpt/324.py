def print_policy(policy, terminal_states):
    
    idx_to_symbol = {0:'\u2190', 1:'\u2191', 2:'\u2192', 3:'\u2193'}
    
    border_str = "\u00B7 "
    for i in range(policy.shape[0]):
        border_str += "\u2015 "
    border_str += "\u00B7 "
    
    for i in range(policy.shape[0]):
        
        string = ""
        for j in range(policy.shape[1]):
            
            if (i,j) in terminal_states:
                string += '\u25A0 '
            else:
                string += idx_to_symbol[policy[i, j]]+" "
        
        print(string)
    
    return