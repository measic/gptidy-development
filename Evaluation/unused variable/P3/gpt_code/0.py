_, _ = plt.subplots(1,2, figsize=(10,4))
_[0].imshow(img_advi)
_[0].set_title("segmented image (ADVI)")
_[1].hist(y, bins=K);
_[1].set_title("cluster assignments (ADVI)")
plt.tight_layout()