def delta_f_trace(list_of_terms, x_value, delta_x):
    initial_f_value = output_at(list_of_terms, x_value)
    delta_f_value = delta_f(list_of_terms, x_value, delta_x)
    if initial_f_value and delta_f_value:
        trace =  trace_values(x_values=[x_value + delta_x, x_value + delta_x], 
                              y_values=[initial_f_value, initial_f_value + delta_f_value], mode = 'lines',
                              name = 'delta f = ' + str(delta_x))
        return trace