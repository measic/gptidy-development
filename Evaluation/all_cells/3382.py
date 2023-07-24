p = 2000
box = (slice(p,p+500), slice(p,p+500))
gt = page_gt[box]
render = diva.color_gt(gt)
plt.imshow(render)
# print(np.unique(gt)) 
[bin(n) for n in np.unique(page_gt)]
np.unique(gt)
# hex(gt[0,0])
# (gt == 1).shape