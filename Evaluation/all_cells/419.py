x_range = Range1d()
y_range = Range1d()

map_options = GMapOptions(lat=39., lng=-98, zoom=3)

plot = GMapPlot(
    x_range=x_range, y_range=y_range,
    map_options=map_options,
    title = "NIST Fire Studies", plot_width=875, plot_height=500
)
plot.map_options.map_type="terrain"