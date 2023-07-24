df_hues = ['Todos','Sin distinguidos Betweenness', 'Sin distinguidos Grado']
gig_comp_degree = gig_comp_graph.degree()
gig_bet_degree = gig_bet_graph.degree()
gig_degree_degree = gig_degree_graph.degree()
degree_frequencies1 = Counter([degree for (author, degree) in gig_comp_degree])
degree_frequencies2 = Counter([degree for (author, degree) in gig_bet_degree])
degree_frequencies3 = Counter([degree for (author, degree) in gig_degree_degree])
degree_info = []
for k,v in degree_frequencies1.iteritems(): degree_info.append((k,v,df_hues[0]))
for k,v in degree_frequencies2.iteritems(): degree_info.append((k,v,df_hues[1]))
for k,v in degree_frequencies3.iteritems(): degree_info.append((k,v,df_hues[2]))
degree_df = pd.DataFrame(degree_info)