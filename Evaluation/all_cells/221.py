img[...]=0
X = (x-400)/30
Y = -(y-300)/30
R = np.sqrt(X**2 + Y**2)
t = np.arctan2(Y,X)
img[R<5]= (1,0,0)
img[(t > 0) & (t<3.14/4)]=(0,0,1)

plt.imshow(img, interpolation="bilinear")