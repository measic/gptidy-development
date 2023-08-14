def calc_sum_product_factor_to_variable_msg(factor, variable):
    neighbour_msg_prod = calc_other_neighbour_msg_prod(factor, variable)
    
    f_neighb_first = move_dimension_first(factor.f, factor.neighbours.index(variable))
    
    return marginalize(calculate_factor(f_neighb_first, neighbour_msg_prod), 0)
