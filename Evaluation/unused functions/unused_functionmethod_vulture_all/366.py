def delta_x_trace(list_of_terms, x_value, delta_x):
    initial_f_value = output_at(list_of_terms, x_value)
    if initial_f_value:
        trace = trace_values(x_values=[x_value, x_value + delta_x],
                            y_values=[initial_f_value, initial_f_value], mode = 'lines', 
                            name = 'delta x = ' + str(delta_x))
        return trace