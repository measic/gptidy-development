# Definimos grafo componente gigante
gig_comp_graph = coauthor_graph.subgraph(gig_comp)

# Seleccionamos 3 nodos random usando random.org y le agregamos a Stephen Hawking
selected_nodes = [list(gig_comp_graph.nodes())[i] for i in [182,202,1083]]
selected_nodes.append("Hawking")
print "Nodos semilla seleccionados: " + str(selected_nodes)

def connected_evolution(G, node):
    nodes = {node}
    difference = [1]
    acum = [1]
    depth = 1
    while len(nodes) < len(G.nodes()):
        newnodes = set(nodes)
        for cur_node in nodes:
            newnodes.update(nx.neighbors(G, cur_node))
        acum.append(len(newnodes))
        difference.append(acum[depth]-acum[depth-1])
        depth = depth+1
        nodes = set(newnodes)
    return (acum, difference)

def annot_max(x,y, ax):
    xmax = x[np.argmax(y)]
    ymax = np.amax(y)
    text= " Maximo: x={0}, y={1}".format(xmax, ymax)
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

def plot_evolution(acum, difference, nodename):
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    sns.barplot(range(0,len(difference)), y=difference, ax=ax1)
    ax1.set_title("Numero de autores nuevos desde el nodo " + nodename)
    ax1.set_xlabel("Distancia del nodo semilla")
    annot_max(range(0,len(difference)), difference, ax1)
    sns.barplot(range(0,len(acum)), y=acum, ax=ax2)
    ax2.set_xlabel("Distancia del nodo semilla")
    ax2.set_title("Numero de autores acumulados alcanzados desde el nodo " + nodename)
    plt.show()

for node in selected_nodes:
    (acum, difference) = connected_evolution(gig_comp_graph, node)
    plot_evolution(acum, difference, node)