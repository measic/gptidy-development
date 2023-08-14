data_x = list(range(5))
data_y = list(range(5, 10))
text = list(range(10, 15))   # texts shown on the data points when hovering over the points; this is not mandatory

show_plot([make_scatter(data_x, data_y, text)], make_layout(500, 500))