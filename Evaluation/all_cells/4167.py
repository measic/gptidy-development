start = datetime.now()
layout = g.layout_fruchterman_reingold()
plt = plot(g, "Tu-154_crash_igraph.pdf", layout=layout, bbox = (15000, 9000), margin = 20)
print("It took {} to generate the layout:".format(datetime.now() - start))