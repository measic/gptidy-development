img[250-10:250+10, 300:400] = (0,0,1)
img[200:300, 350-10:350+10] = (0,0,1)
plt.imshow(img[200:400, 300:500], interpolation='bilinear')