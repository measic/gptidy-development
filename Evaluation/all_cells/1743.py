# Test to see if DW comp. is working
imbalance, bicoloring = dnx.structural_imbalance(G, sampler)
frustration_score = len(list(imbalance.keys()))/G.number_of_edges()