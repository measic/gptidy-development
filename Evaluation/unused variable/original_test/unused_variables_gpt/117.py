edge_cols = []
for edge in G.edges(data=True):
    if edge[2]["sign"] == -1:
        edge_cols.append("red")
    else:
        edge_cols.append("green")

fig, ax = plt.subplots(figsize=(15, 10))
nx.draw_shell(G, ax=ax, with_labels=True, node_size=1000, node_color="white", 
              edge_color=edge_cols)