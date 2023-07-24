coauthor_graph = nx.Graph()
for index, row in df.iterrows():
    paper_authors = row['authors'].split("&")
    paper_authors = map(lambda x: x.strip(),paper_authors)
    paper_authors_pairs = list(itertools.combinations(paper_authors, 2))
    coauthor_graph.add_nodes_from(paper_authors)
    coauthor_graph.add_edges_from(paper_authors_pairs)