author_degree_list = list(coauthor_graph.degree())
degree_list = [degree for (author, degree) in author_degree_list]

degree_frequencies = Counter(degree_list)
print degree_frequencies