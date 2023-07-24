start = datetime.now()
layout = g.layout_fruchterman_reingold()
plt = plot(g, layout=layout, bbox = (500, 300), margin = 20)
print("It took {} to generate the layout:".format(datetime.now() - start))
plt