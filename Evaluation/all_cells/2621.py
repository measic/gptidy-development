fig, axs = plt.subplots(2,2, figsize=(10,6))
axs[0][0].imshow(img_mcmc)
axs[0][0].set_title("Shared prior: segmented image (MCMC)")
axs[0][1].hist(clusters, bins=K);
axs[0][1].set_title("Shared prior: cluster assignments (MCMC)")
axs[1][0].imshow(img_mcmc_2)
axs[1][0].set_title("Different pior: segmented image (MCMC)")
axs[1][1].hist(clusters_2, bins=K);
axs[1][1].set_title("Different prior: cluster assignments (MCMC)")
plt.tight_layout()