import imageio
im = imageio.imread('/home/ivan/Área de trabalho/2017/01/01/BSIU2580749/20170101002612000ES_stamp.jpg')
print(im.shape)
im = im[:,:,0]
print(im.shape)
print(im)

print(['123', *(1, 2, 3)])