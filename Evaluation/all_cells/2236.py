p = graphs.get_plot(x_color='#ff6300', y_color='#19a974', hover_format='{0.[00]}')
p.title.text = '100 x- en y-waarden van f(x)'
p.title.text_font = 'Quicksand'
p.title.text_font_size = '18pt'
p.title.align = 'center'

x1s = np.arange(-1, 9, 0.01).tolist()
y1s = [f(x) for x in x1s]
p.circle(x1s, y1s, radius=.2, color='#555555', alpha=0.4)
p.tools[0].mode = 'vline' # Trigger hover on vertical lines


# x2s = np.arange(-2, 10, 0.1).tolist()
# y2s = [f(x) for x in x2s]
# p.line(x2s, y2s, line_width=4, line_color='#e7040f')

item = json.dumps(json_item(p))
Path('plt/loads_of_x.json').write_text(item)