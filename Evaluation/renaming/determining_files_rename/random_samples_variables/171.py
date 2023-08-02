pred_f = pred_f_te.flatten()[dataset_subset_indices]
pred_t = pred_t_te.flatten()[dataset_subset_indices]
probas_gmm_c = imgs_stretch_eq([probas_gmm[..., np.newaxis]])[0, ..., 0]
variable_def = plt.cm.YlOrRd(1 - probas_gmm_c)[:, :3][dataset_subset_indices]
c_thresh_t = plt.cm.YlOrRd((probas_gmm_c[dataset_subset_indices] < np.sort(probas_gmm_c[dataset_subset_indices])[200]) * 255)[:, :3]
c_thresh_f = plt.cm.YlOrRd((probas_gmm_c[dataset_subset_indices] > np.sort(probas_gmm_c[dataset_subset_indices])[200]) * 255)[:, :3]
_, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].scatter(tsne_all[:, 0][pred_t], tsne_all[:, 1][pred_t], c=variable_def[pred_t], alpha=0.6)
axes[1].scatter(tsne_all[:, 0][pred_t], tsne_all[:, 1][pred_t], c=c_thresh_t[pred_t])
axes[0].scatter(tsne_all[:, 0][pred_f], tsne_all[:, 1][pred_f], c=variable_def[pred_f], marker='x')
axes[1].scatter(tsne_all[:, 0][pred_f], tsne_all[:, 1][pred_f], c=c_thresh_f[pred_f], marker='x')