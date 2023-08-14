train_path = "../BSR/BSDS500/data/images/train/"
img_no = 2092
img = plt.imread(train_path+"{0:d}.jpg".format(img_no))
plt.imshow(img)
print("image shape:", img.shape)