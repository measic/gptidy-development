connected_components = nx.connected_components(coauthor_graph)
max_size = 0
count = 0
gig_comp = []
for comp in connected_components:
    if (len(comp) > max_size):
        max_size = len(comp)
        gig_comp = comp
    count += 1

print "Hay " + str(count) + " componentes conexas."
print "La mayor componente conexa tiene " + str(max_size) + " nodos."