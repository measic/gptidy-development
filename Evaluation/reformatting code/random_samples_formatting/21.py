### Preprocess the data here. Preprocessing steps could include normalization, converting to grayscale, etc.
### Feel free to use as many code cells as needed.

def rgb2gray(rgb):
    gray_img = cv.cvtColor(rgb,cv.COLOR_BGR2GRAY)
    return np.asarray(gray_img)

# Normalization
def normalize(img):
    return cv.normalize(img, img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)

# Find the darkest image in training data
img_sums = [sum(sum(rgb2gray(img))) for img in X_train]
min_ind = np.argmin(img_sums)
print(min_ind)

f, axarr = plt.subplots(1, 2, figsize=(8, 4))
axarr[0].imshow(X_train[min_ind], cmap="gray")
axarr[0].set_title('Before normalization')

normalized_gray = normalize(X_train[min_ind])
axarr[1].imshow(normalized_gray, cmap="gray")
axarr[1].set_title('After normalization')

# Normalize all training, validation data
# Gray all images
X_train = [rgb2gray(img) for img in X_train]
X_train = [normalize(img) for img in X_train]

rand_img_indices = plot_imgs(X_train, y_train)
print(rand_img_indices)