print("MCMC:")
cluster_metric(gt_seg.flatten(), clusters_2)
print("\nADVI:")
cluster_metric(gt_seg.flatten(), y_2)