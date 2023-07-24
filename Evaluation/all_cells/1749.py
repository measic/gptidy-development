edge_cols = []
frustrated_edges = imbalance.keys()
for edge in G.edges(data=True):
    if (edge[0],edge[1]) in frustrated_edges:
        edge_cols.append("black")
    elif edge[2]["sign"] == -1:
        edge_cols.append("red")
    else:
        edge_cols.append("green")

fig,ax = plt.subplots(figsize=(15,10))
nx.draw_networkx(G, pos=nx.drawing.layout.bipartite_layout(G, nodes_one), ax=ax, 
                 with_labels=True, node_size=1000, node_color="white", edge_color=edge_cols)