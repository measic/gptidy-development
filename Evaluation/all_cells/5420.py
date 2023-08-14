### Load the images and plot them here.
### Feel free to use as many code cells as needed.
import glob
import matplotlib.image as mpimg
import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import random
from sklearn.utils import shuffle
import tensorflow as tf

fig, axs = plt.subplots(2,3, figsize=(10, 6))
fig.subplots_adjust(hspace = .2, wspace=.001)
axs = axs.ravel()

my_images = []

for i, img in enumerate(glob.glob('./my-signs/*.png')):
    image = cv.imread(img)
    axs[i].axis('off')
    axs[i].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    image = cv.resize(image, (32,32))
    my_images.append(image)

my_images = np.asarray(my_images)
print(my_images.shape)