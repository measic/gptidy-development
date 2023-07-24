path = "input\\layouts\\bepo.txt"
mapping = create_map_from_txt(path)
objective, p, a, f, e = get_objectives(mapping, 0.0, w_a, w_f, w_e, level_cost, corpus_weights, quadratic=1)
print "Bépo score: %f\n Performance: %f\n Association: %f\n Familiarity: %f\n Ergonomics: %f\n"%(objective, p, a, f, e)