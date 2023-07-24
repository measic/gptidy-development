from graph import plot, trace_values

trace_delta_x_four_x_plus_fifteen = delta_x_trace(four_x_plus_fifteen, 2, 1)
if four_x_plus_fifteen_trace and trace_delta_f_four_x_plus_fifteen and trace_delta_x_four_x_plus_fifteen:
    plot([four_x_plus_fifteen_trace, trace_delta_f_four_x_plus_fifteen, trace_delta_x_four_x_plus_fifteen], {'title': '4x + 15'})