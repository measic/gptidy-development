# Genere un grafo aleatorio con la misma distribucion de grado y compute las mismas medidas para este grafo
gig_comp_degrees = [degree for (node, degree) in gig_comp_graph.degree()]
random_degree_graph = nx.random_degree_sequence_graph(gig_comp_degrees)