variable_def = 200
dataset_subset_indices = get_balanced_subset_indices(data_test.gt_patches.flatten(), np.arange(1, 9), pts_per_class=variable_def)
dataset_subset_indices = np.concatenate(dataset_subset_indices)