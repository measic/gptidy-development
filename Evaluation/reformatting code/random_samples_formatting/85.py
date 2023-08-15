def removal_evolution(removal_list, G):
    disting_bet_average_degree = []
    hist = nx.degree_histogram(G)
    last_average_degree = float(sum(hist[i] * i for i in range(len(hist)))) / float(sum(hist))
    idx_node = 0
    while last_average_degree > 0 and idx_node < len(removal_list):
        disting_bet_average_degree.append(last_average_degree)
        hist = nx.degree_histogram(G)
        last_average_degree = float(sum(hist[i] * i for i in range(len(hist)))) / float(sum(hist))
        G.remove_node(removal_list[idx_node][0])
        idx_node = idx_node + 1
    return disting_bet_average_degree