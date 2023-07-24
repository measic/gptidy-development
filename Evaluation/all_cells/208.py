img[...]  = 1
img[300:450, 100:700] = (1,0,0)
cx,cy = 250, 450
img[(x-cx)**2+(y-cy)**2<80**2]=1
img[(x-cx)**2+(y-cy)**2<70**2]=0
img[(x-cx)**2+(y-cy)**2<50**2]=0.5
img[(x-cx)**2+(y-cy)**2<20**2]=(0,0,1)

cx,cy = 550, 450
img[(x-cx)**2+(y-cy)**2<80**2]=1
img[(x-cx)**2+(y-cy)**2<70**2]=0
img[(x-cx)**2+(y-cy)**2<50**2]=0.5
img[(x-cx)**2+(y-cy)**2<20**2]=(0,0,1)
img[200:300, 500:600] = 1
yy,xx = np.indices((100,100))
img[200:300, 500:600][yy>xx] = (1,0,0)

plt.imshow(img, interpolation='bilinear')
