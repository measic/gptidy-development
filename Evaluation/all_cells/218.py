img[...] = 0
line1 = y - (400-0.7*x)
line2 = y - (400+0.7*(x-800))
img[line1 * line2 > -5000] =1

plt.imshow(img, interpolation="bilinear")