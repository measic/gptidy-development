f, (ax1, ax2) = plt.subplots(2, 4, figsize=(24, 9))
f.tight_layout()
half = 4
for i in range(4):
    ax1[i].imshow(sample_data[i])
    ax2[i].imshow(sample_data[half + i])
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()