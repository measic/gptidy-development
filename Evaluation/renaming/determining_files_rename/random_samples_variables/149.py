tsne_pts_per_class = 200
variable_def = get_balanced_subset_indices(data_test.gt_patches.flatten(), np.arange(1, 9), pts_per_class=tsne_pts_per_class)
variable_def = np.concatenate(variable_def)