ot_model_gr2 = wot.ot.OTModel(adata, epsilon=0.05, lambda1=1, lambda2=50, growth_iters=2)
tmap_anno_gr2 = ot_model_gr2.compute_transport_map(7, 7.5)