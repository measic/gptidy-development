def get_color(community):
    """
    get_color() is a simple function to return the color for a node or edge 
    """
    color_dict = {
        0: "#df0eff", #pro-gov
        1: "#0ec4ff", #opposition
        2: "#4c463e", #centrists
        3: "#73c400" #youths
    } 
    return color_dict[community] if community in color_dict else "#aaa194"

def prepare_graph(g):
    """
    prepare_graph() changes node and edge sizes and assigns color as chosen in the get_color() color dictionary
    """
    nodes_to_delete = []
    for vertex in g.vs:
        if vertex.indegree() == 0:
            nodes_to_delete.append(vertex.index)
        else:
            vertex['size'] = vertex.indegree()/100000
            vertex['color'] = get_color(vertex['im'])
    g.delete_vertices(nodes_to_delete)

    for edge in g.es:
        tup = edge.tuple
        edge['size'] = 0.1
        edge['arrow_size'] = None
        edge['curved'] = 0.2
        if len(tup) == 2:
            if tup[0] == tup[1]:
                edge['color'] = get_color(tup[0])
            else:
                if g.vs[tup[0]].indegree() > g.vs[tup[1]].indegree():
                    edge['color'] = get_color(g.vs[tup[0]]['im'])
                elif g.vs[tup[0]].indegree() < g.vs[tup[1]].indegree():
                    edge['color'] = get_color(g.vs[tup[1]]['im'])
                else:
                    edge['color'] = 'black'
    return g
    
g = prepare_graph(g)