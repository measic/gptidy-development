# Agarramos el 1% mas destacado de los nodos segun betweenness y grado
disting_bound = len(gig_comp_graph.nodes()) / 50

disting_bet = dict(sorted(betweenness_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:disting_bound])

disting_degree = dict(sorted(degree_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:disting_bound])

print "Nodos distinguidos segun Betweenness:"
print disting_bet.keys()

print "\n"

print "Nodos distinguidos segun Grado:"
print disting_degree.keys()