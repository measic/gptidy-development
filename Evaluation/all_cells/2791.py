def generate_graphs(n=10, prog='neato', multi=True):
    d = {}
    for i in range(n):
        max_nodes = np.random.randint(3, 8)
        max_iter = np.random.randint(10, 100)
        
        if multi is True:
            g, p = generate_multi_bbn(max_nodes, max_iter=max_iter) 
        else: 
            g, p = generate_singly_bbn(max_nodes, max_iter=max_iter)
            
        bbn = convert_for_exact_inference(g, p)
        pos = nx.nx_agraph.graphviz_layout(g, prog=prog)
        
        d[i] = {
            'g': g,
            'p': p,
            'bbn': bbn,
            'pos': pos
        }
    return d

def draw_graphs(graphs, prefix):
    fig, axes = plt.subplots(5, 2, figsize=(15, 20))
    for i, ax in enumerate(np.ravel(axes)):
        graph = graphs[i]
        nx.draw(graph['g'], pos=graph['pos'], with_labels=True, ax=ax)
        ax.set_title('{} Graph {}'.format(prefix, i + 1))

multi_graphs = generate_graphs(multi=True)
singly_graphs = generate_graphs(multi=False)