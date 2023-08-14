import math
y1s = np.arange(0, 10, 0.1).tolist()
x1s = [(1/5)*y**2 - 5 for y in y1s]
y2s = np.arange(-5, 0, 0.1).tolist()
x2s = [(1/5)*y**2 - 5 for y in y2s]

p = graphs.get_plot()
p.title.text = 'Grafiek van een niet-functie'
p.title.text_font = 'Quicksand'
p.title.text_font_size = '18pt'
p.title.align = 'center'

p.tools[0].mode = 'vline' # Trigger hover on vertical lines
p.line(x1s, y1s, line_width=10, color=graphs.BLUE, line_cap='round')
p.line(x2s, y2s, line_width=10, color=graphs.BLUE, line_cap='round')
item = json.dumps(json_item(p))
Path('plt/no_fx.json').write_text(item)