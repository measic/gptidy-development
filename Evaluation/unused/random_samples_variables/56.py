# Test to see if DW comp. is working
corr_mat = corr_tensor[30, :, :].copy()
        
corr_mat[(corr_mat > -1*0.7) & (corr_mat < 0.7)] = 0
G, density = make_graph(corr_mat, nodes, 'signed')