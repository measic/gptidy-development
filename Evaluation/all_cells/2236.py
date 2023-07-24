from hoezithet import graphs

xs = [5]
ys = [f(x) for x in xs]

p = graphs.get_plot(x_color='#ff6300', y_color='#19a974')
p.title.text = 'x en y als coördinaat'
p.title.text_font = 'Quicksand'
p.title.text_font_size = '18pt'
p.title.align = 'center'
p.circle(xs, ys, radius=.4, color='#555555')

item = json.dumps(json_item(p))
Path('./plt/single_x.json').write_text(item)