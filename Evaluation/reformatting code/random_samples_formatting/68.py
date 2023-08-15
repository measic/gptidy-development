with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    
    draw_graphs(multi_graphs, 'Multi-connected')
    draw_graphs(singly_graphs, 'Singly-connected')