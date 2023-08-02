from skimage.io import imread
from skimage import feature
ct = imread('https://upload.wikimedia.org/wikipedia/commons/5/5f/MRI_EGC_sagittal.png')[-1::-1, :, :]
variable_def = feature.canny(ct[:, :, 0], low_threshold=0.1 * 255, high_threshold=0.4 * 255) * 255
plt.figure(figsize=[10, 10])
plt.imshow(variable_def[-1::-1, :])