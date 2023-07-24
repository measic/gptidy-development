img[...] = 0
curve1 = y<np.floor(500-0.001*(x-400)**2)
curve2 = y>np.floor(400-0.0005*(x-400)**2)

img[curve1 & curve2] = (1,0,0)

plt.imshow(img, interpolation="bilinear")