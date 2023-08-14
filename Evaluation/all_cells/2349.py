heights = N.array([o['center'][2] for o in collection])
rng = [heights.min(),heights.max()]

for o in collection:
    ix = N.interp(o['center'][2], rng, [0,6])
    o['color'] = cmap.hex_colors[6-int(ix)]