def derivative_trace(list_of_terms, x_value, line_length = 4, delta_x = .01):
    derivative_at = derivative_of(list_of_terms, x_value, delta_x)
    y = output_at(list_of_terms, x_value)
    if derivative_at and y:
        x_minus = x_value - line_length/2
        x_plus = x_value + line_length/2
        y_minus = y - derivative_at * line_length/2
        y_plus = y + derivative_at * line_length/2
        return trace_values([x_minus, x_value, x_plus],[y_minus, y, y_plus], name = "f' (x) = " + str(derivative_at), mode = 'lines')