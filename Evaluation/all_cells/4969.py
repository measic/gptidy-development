import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import plot, trace_values, build_layout

x_values = list(range(0, 6))
# layout = build_layout(y_axis = {'range': [0, 35]})


four_x_plus_fifteen_values = list(map(lambda x: output_at(four_x_plus_fifteen, x),x_values))
four_x_plus_fifteen_trace = trace_values(x_values, four_x_plus_fifteen_values, mode = 'lines')
plot([four_x_plus_fifteen_trace])