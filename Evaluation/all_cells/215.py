img[...] = 0
sine_wave = np.floor(300+200*np.sin(x/800*2*np.pi))

img[ (y<sine_wave+2) &  (y>sine_wave-2)] = 1
plt.imshow(img, interpolation="bilinear")