from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, plot

movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')

plot([movies_trace])