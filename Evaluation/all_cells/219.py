img[...]=0
X = (x-400)/200
Y = -(y-300)/200
img[(X**2+Y**2-1)**3-X**2 * Y**3<0]= (1,0,0)

plt.imshow(img, interpolation="bilinear")