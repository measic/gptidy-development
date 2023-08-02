fig, axs = plt.subplots(1,2, figsize=(10,4))
axs[0].imshow(img_advi)
axs[0].set_title("segmented image (ADVI)")
axs[1].hist(y, bins=K);
axs[1].set_title("cluster assignments (ADVI)")
plt.tight_layout()