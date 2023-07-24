delta_x = 1

# derivative_traces(list_of_terms, x_value, line_length = 4, delta_x = .01)

three_x_plus_tangents = delta_traces(four_x_plus_fifteen, 2, line_length= 2*1, delta_x = delta_x)

# only plot the list of traces, if three_x_plus_tangents, does not look like [None, None, None]
if list(filter(None.__ne__, three_x_plus_tangents)):
    plot([four_x_plus_fifteen_trace, *three_x_plus_tangents])