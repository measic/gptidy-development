xpos, ypos, size = 0,700, 500 
box = (xpos,ypos,xpos+size,ypos+size)
plt.imshow(hisdb[0][0].crop(box))