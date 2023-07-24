# tsne
tsne_train = tsne_all[(tsne_y == y_pred_label_te.flatten()[dataset_subset_indices]) & tsne_y!=0]
tsne_train_y = tsne_y[(tsne_y == y_pred_label_te.flatten()[dataset_subset_indices]) & tsne_y!=0]
# plot
_, ax = plt.subplots(1, 1, figsize=(10, 10))
plt.axis('off')
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plot_pts_2d(tsne_all, tsne_y, ax, classes_to_keep, colors)
plt.savefig("../Figures/Zurich/tSNE/t-SNE_ED_after_PCA.pdf",
            bbox_inches='tight', pad_inches=0)