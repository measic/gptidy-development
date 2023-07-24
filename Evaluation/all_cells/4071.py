nodes_visible = random.sample(coauthor_graph.nodes(), 1000)
nx.draw_networkx(coauthor_graph, with_labels=False, node_size=10, nodelist = nodes_visible)
plt.tick_params(axis='x', labelbottom='off')
plt.tick_params(axis='y', labelleft='off')
plt.title("Grafo de Co-autorias")
plt.rcParams["figure.figsize"] = [14,6]
plt.show()