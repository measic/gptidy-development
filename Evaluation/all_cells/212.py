img[...]  = 0
cx,cy = 300, 300
circle1 = (x-cx)**2+(y-cy)**2<150**2
cx,cy = 500, 300
circle2 = (x-cx)**2+(y-cy)**2<150**2
img[:,:, 0][circle1]=1
img[:,:, 1][circle2]=1
img[circle1 | circle2] =(0,0,1)
plt.imshow(img, interpolation='bilinear')
