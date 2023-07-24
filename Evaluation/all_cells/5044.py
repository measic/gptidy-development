from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, m_b_trace, plot
if x_values and y_values:
    movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    regression_trace = m_b_trace(1.7, 10, x_values, name='estimated revenue')
    plot([movies_trace, regression_trace, error_at_120m])