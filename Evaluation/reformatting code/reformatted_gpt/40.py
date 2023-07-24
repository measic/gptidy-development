from graph import make_subplots, trace_values, plot_figure


def function_values_trace(list_of_terms, x_values):
    function_values = list(map(lambda x: output_at(list_of_terms, x), x_values))
    return trace_values(x_values, function_values, mode='lines')


def derivative_values_trace(list_of_terms, x_values, delta_x):
    derivative_values = list(map(lambda x: derivative_of(list_of_terms, x, delta_x), x_values))
    return trace_values(x_values, derivative_values, mode='lines')


def function_and_derivative_trace(list_of_terms, x_values, delta_x):
    traced_function = function_values_trace(list_of_terms, x_values)
    traced_derivative = derivative_values_trace(list_of_terms, x_values, delta_x)
    return make_subplots([traced_function], [traced_derivative])


four_x_plus_fifteen_function_and_derivative = function_and_derivative_trace(four_x_plus_fifteen, list(range(0, 7)), 1)

plot_figure(four_x_plus_fifteen_function_and_derivative)