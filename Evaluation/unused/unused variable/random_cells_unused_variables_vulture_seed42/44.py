disting_bet_all = sorted(betweenness_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
disting_degree_all = sorted(degree_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
disting_bet_graph = gig_comp_graph.copy(as_view=False)
disting_degree_graph = gig_comp_graph.copy(as_view=False)

bet_removal_evolution = removal_evolution(disting_bet_all, disting_bet_graph)
degree_removal_evolution = removal_evolution(disting_degree_all, disting_degree_graph)