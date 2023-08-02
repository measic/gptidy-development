# Bokeh options for interaction
TOOLS="pan,box_zoom,reset,resize,save,hover"

# Read in example log file
log_data = pd.read_csv('log_file.csv', index_col=0)
time_x = log_data.iloc[ : , 1]
T_data = log_data.iloc[ : , 2]
HF_data = log_data.iloc[ : , 3]

# Format plots and display data
p1 = figure(title='FF Helmet - Ambient Temp', x_axis_label = 'Time (s)', y_axis_label = 'Temperature (°C)', 
            tools=TOOLS, plot_width=750, plot_height=500)
p1.line(time_x, T_data, color='red', line_width = 3, legend='Amb T')

p2 = figure(title='FF Helmet - Heat Flux', x_axis_label = 'Time (s)', y_axis_label = 'Heat Flux (kW/m²)', 
            tools=TOOLS, plot_width=750, plot_height=500)
p2.line(time_x, HF_data, color='blue', line_width = 3, line_dash = 'dashed', legend='Heat Flux')

p = vplot(p1, p2)