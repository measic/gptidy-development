boximg   = hisdb[0][0].crop(box)
boxgtimg = hisdb[0][1].crop(box)
plt.imshow(mark_boundaries(np.array(boximg),
                           np.array(boxgtimg)[:,:,2]))