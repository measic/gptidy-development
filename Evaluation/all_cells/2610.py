fig, axs = plt.subplots(1,2, figsize=(10,4))
axs[0].imshow(img_mcmc)
axs[0].set_title("segmented image (MCMC)")
axs[1].hist(clusters, bins=K);
axs[1].set_title("cluster assignments (MCMC)")
plt.tight_layout()