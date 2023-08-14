plt.rcParams["axes.grid"] = False
fig, axs = plt.subplots(1,3, figsize=(12,12))
axs[0].imshow(img_advi_2)
axs[0].set_title("segmented image (ADVI)")
axs[1].imshow(img_mcmc_2)
axs[1].set_title("segmented image (MCMC)")
axs[2].imshow(img)
axs[2].set_title("original image")
plt.tight_layout()