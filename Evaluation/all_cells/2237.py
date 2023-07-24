import numpy as np

xs = np.arange(-1, 6, 1).tolist()
xs = sorted(xs)
ys = [f(x) for x in xs]

p = graphs.get_plot(x_color='#ff6300', y_color='#19a974')
p.title.text = '7 x- en y-waarden van f(x)'
p.title.text_font = 'Quicksand'
p.title.text_font_size = '18pt'
p.title.align = 'center'
p.circle(xs, ys, radius=.4, color='#555555')

item = json.dumps(json_item(p))
Path('plt/multiple_x.json').write_text(item)