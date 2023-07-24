# Create graph for each month and calculate frustration. 

frustration_array = []
bicoloring_array = []
date_array = []
density_array = []
threshold_array = []

count = 0
for i in np.arange(0.7, 1, 0.1):
    for j in range(1, int(num_examples/5)):
        
        corr_mat = corr_tensor[j*5, :, :].copy()
        corr_mat[(corr_mat > -1*i) & (corr_mat < i)] = 0
        
        G, density = make_graph(corr_mat, nodes, 'signed')

        try:
            opt_imbalance, opt_bicoloring = dnx.structural_imbalance(G, sampler)
            opt_score = len(list(imbalance.keys()))/G.number_of_edges()
            
            if opt_score > 0.00:
                for k in range(3):
                    imbalance, bicoloring = dnx.structural_imbalance(G, sampler)
                    frustration_score = len(list(imbalance.keys()))/G.number_of_edges()
                    
                    if frustration_score < opt_score:
                        opt_imbalance = imbalance
                        opt_bicoloring = bicoloring
                        opt_score = frustration_score
                        
            count += 1
            
            if count % 10 == 0:
                print("iteration: i = %f, j = %d" % (i,j))
                
        except Exception as err:
            print(err)
            print("No soln found for threshold %f and matrix %d" % (i, int(j*5)))
        else:
            threshold_array.append(i)
            frustration_array.append(opt_score)
            bicoloring_array.append(opt_bicoloring)
            density_array.append(density)
            date_array.append(dates[j*5])
            