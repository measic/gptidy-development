start = datetime.now()
layout = g.layout_fruchterman_reingold() #choose layout
plt = plot(g, layout=layout, bbox = (500, 300), margin = 20) #plot the graph with the layout
#bbox specifies size of the image (horiontal, vertical), and margin specifies space around the image
print("It took {} to generate the layout:".format(datetime.now() - start)) #we will time the computer to see how long it takes
plt