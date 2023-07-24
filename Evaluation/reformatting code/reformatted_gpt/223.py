### Load the images and plot them here.
### Feel free to use as many code cells as needed.
from PIL import Image
import glob
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import numpy as np

test_images = []
for filename in glob.glob('test_img/*.png'):  # assuming gif
    im = cv2.imread(filename)
    test_images.append(im)