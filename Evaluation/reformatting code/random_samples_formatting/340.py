selem = square(3)
ct_close = erosion(dilation(canny,selem=selem),selem=selem)
plt.figure(figsize=[10,10])
plt.imshow(ct_close[-1::-1,:]);