# visualization

# show image of DF uncertainty vs. max margin uncertainty
for img_idx in range(5):
    acc_im_df = convert_patches_to_image(data_test.imgs, probas_patches_df[..., np.newaxis], img_idx, 64, 64, 0)
    acc_im_df = imgs_stretch_eq([acc_im_df])[0]
    plt.figure(figsize=(8, 8))
    plt.imshow(acc_im_df[..., 0], cmap='RdYlGn')
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig("../Figures/Zurich/Im_cert/ED/df_im_" + str(img_idx) + ".pdf", 
                    bbox_inches='tight', pad_inches=0)
    plt.close()