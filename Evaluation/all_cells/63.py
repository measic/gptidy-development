from skimage.io import imread
from skimage import feature

ct = imread('https://upload.wikimedia.org/wikipedia/commons/5/5f/MRI_EGC_sagittal.png')[-1::-1,:,:]
canny = feature.canny(ct[:,:,0],low_threshold=.1*255,high_threshold=.4*255)*255

plt.figure(figsize=[10,10])
plt.imshow(canny[-1::-1,:]);