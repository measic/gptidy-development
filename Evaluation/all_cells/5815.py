### Load the images and plot them here.
### Feel free to use as many code cells as needed.

import matplotlib.image as mpimg
import glob
# images = glob.glob('../german_traffic_signs/*')

# squeezed = []
# for image in images:
img = mpimg.imread('Zeichen_206.svg')
sqimg = img.squeeze()


plt.figure(figsize=(1,1))
plt.imshow(sqimg)
