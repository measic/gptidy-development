plt.figure(figsize=(20, 60))
for i in range(1, 97):
    plt.subplot(24, 4, i)
    plt.imshow(imgs[i][0], cmap='gray')
    bbox = bboxes[i]
    plt.gca().add_patch(matplotlib.patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], ec='r', fc='none'))
    plt.annotate(imgs[i][1], (0, 0))