f, (ax1, ax2) = plt.subplots(2, 3, figsize=(24, 9))
f.tight_layout()
half = 3
for i in range(3):
    ax1[i].imshow(test_images[i])
    ax2[i].imshow(test_images[half + i])
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()