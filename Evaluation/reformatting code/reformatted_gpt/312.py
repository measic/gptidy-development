import matplotlib.pyplot as plt

f = plt.figure()
plt.imshow(oriImg[:, :, [2, 1, 0]])
ax2 = plt.imshow(heatmap_avg[:, :, 1], alpha=0.5)
f.show()