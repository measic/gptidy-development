img[...] = 0
sine_wave = np.floor(300+200*np.sin(x/800*2*np.pi))

img[ (y<sine_wave) &  (y >300)] = (1,0,0)
img[ (y>sine_wave) &  (y <300)] = (0,0,1)
plt.imshow(img, interpolation="bilinear")