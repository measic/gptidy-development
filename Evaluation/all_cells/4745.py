# plot first 2 PCA components
_, ax = plt.subplots(1, 1, figsize=(8, 8))
plot_pts_2d(act_test[:, :2], data_test.gt_patches.flatten(), ax, classes_to_keep, colors, subsample_pct=.0005)
ax.set_axis_off()
print("Variance explained by first 2 components: %.2f" % np.sum(pca.explained_variance_ratio_[:2]))