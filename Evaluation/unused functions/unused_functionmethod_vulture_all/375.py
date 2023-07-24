def calc_sum_product_variable_to_factor_msg(variable, factor):
    
    neighbour_msg_prod = get_neighbour_messages(variable, factor)
    
    if len(neighbour_msg_prod) > 0:
        return np.prod(np.array(neighbour_msg_prod), axis=0)
    else:
        return np.ones(variable.num_states)
    