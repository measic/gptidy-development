probas_patches_msr = np.reshape(get_acc_net_msr(y_pred_te).flatten(), np.shape(data_test.gt_patches))
probas_patches_msr -= np.min(probas_patches_msr)
probas_patches_msr /= np.max(probas_patches_msr)
probas_patches_margin = np.reshape((1 - get_acc_net_max_margin(y_pred_te)).flatten(), np.shape(data_test.gt_patches))
probas_patches_margin -= np.min(probas_patches_margin)
probas_patches_margin /= np.max(probas_patches_margin)
probas_patches_entropy = np.reshape((1 - get_acc_net_entropy(y_pred_te)).flatten(), np.shape(data_test.gt_patches))
probas_patches_entropy -= np.min(probas_patches_entropy)
probas_patches_entropy /= np.max(probas_patches_entropy)
probas_patches_msr = np.reshape(get_acc_net_msr(y_pred_te).flatten(), np.shape(data_test.gt_patches))
probas_patches_msr -= np.min(probas_patches_msr)
probas_patches_msr /= np.max(probas_patches_msr)
probas_patches_margin = np.reshape((1 - get_acc_net_max_margin(y_pred_te)).flatten(), np.shape(data_test.gt_patches))
probas_patches_margin -= np.min(probas_patches_margin)
probas_patches_margin /= np.max(probas_patches_margin)
probas_patches_entropy = np.reshape((1 - get_acc_net_entropy(y_pred_te)).flatten(), np.shape(data_test.gt_patches))
probas_patches_entropy -= np.min(probas_patches_entropy)
probas_patches_entropy /= np.max(probas_patches_entropy)
acc_im_msr = convert_patches_to_image(data_test.imgs, probas_patches_msr[..., np.newaxis], 64, 64)
acc_im_margin = convert_patches_to_image(data_test.imgs, probas_patches_margin[..., np.newaxis], 64, 64)
variable_def = convert_patches_to_image(data_test.imgs, probas_patches_entropy[..., np.newaxis], 64, 64)
for img_idx in range(5):
    plt.figure(figsize=(8, 8))
    plt.imshow(acc_im_msr[img_idx], cmap='RdYlGn')
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('../Figures/Zurich/Im_cert/ED/net_msr_im_' + str(img_idx) + '.pdf', bbox_inches='tight', pad_inches=0)
    plt.close()
    plt.figure(figsize=(8, 8))
    plt.imshow(acc_im_margin[img_idx], cmap='RdYlGn')
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('../Figures/Zurich/Im_cert/ED/net_margin_im_' + str(img_idx) + '.pdf', bbox_inches='tight', pad_inches=0)
    plt.close()
    plt.figure(figsize=(8, 8))
    plt.imshow(variable_def[img_idx], cmap='RdYlGn')
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('../Figures/Zurich/Im_cert/ED/net_entropy_im_' + str(img_idx) + '.pdf', bbox_inches='tight', pad_inches=0)
    plt.close()