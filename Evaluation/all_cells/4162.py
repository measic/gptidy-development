for edge in g.es:
    tup = edge.tuple
    edge['curved'] = 0.2 #lets also curve the links so that it looks better
    if len(tup) == 2:
        if tup[0] == tup[1]:
            edge['color'] = color_dict[tup[0]]
        else:
            if g.vs[tup[0]].indegree() > g.vs[tup[1]].indegree():
                edge['color'] = color_dict[g.vs[tup[0]]['community']]
            elif g.vs[tup[0]].indegree() < g.vs[tup[1]].indegree():
                edge['color'] = color_dict[g.vs[tup[1]]['community']]
            else:
                edge['color'] = 'black'

#great, lets try to see if that worked with one node:
g.es[0]