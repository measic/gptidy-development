plt.figure(figsize=(20, 60))
for i in range(1, 97):
    plt.subplot(24, 4, i)
    im = np.array((imgs[i][0], imgs[i][0], imgs[i][0]))
    im = im.swapaxes(1, 2)
    im = im.swapaxes(0, 2)
    bbox = bboxes[i] 
    #print(bbox)
    #print(im.shape)
    #print(im)
    #print(im[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[0])+4])
    #im[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[0])+5, 0] = 0
    #im[int(bbox[1]):int(bbox[1])+5, int(bbox[0]):int(bbox[2]), 0] = 0
    #im[int(bbox[1]):int(bbox[3]), int(bbox[2])-5:int(bbox[2]), 0] = 0
    #im[int(bbox[3])-5:int(bbox[3]), int(bbox[0]):int(bbox[2]), 0] = 0
    #print(im[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[0])+4])
    #im[0:200, 0:200] = 0
    plt.imshow(im, cmap='gray')
    #plt.gca().add_patch(matplotlib.patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], ec='r', fc='none'))
    plt.annotate(imgs[i][1], (0, 0))