img[:, :, 2]  = 1-y/600
img[:, :,  0]  = 0.5+y/600*0.5
img[:, :,  1]  = 0.5+y/600*0.5

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

y_bound = (y>200) & (y<300)
x_bound = abs(x-400)< y-100
img[x_bound & y_bound] = (1,0,0)
y_bound = (y>220) & (y<280)
x_bound = abs(x-400)< y-120
img[x_bound & y_bound] = 0
img[200:300, 390:410]=(1,0,0)
plt.imshow(img)