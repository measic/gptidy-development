def convert_to_gray_scale(X, b = [0.299,0.587,0.114]):
    return np.inner(X, b)

def norm_image(image):
    image = convert_to_gray_scale(image).reshape(-1, image_size, image_size, 1)
    image = image/255 - 0.5
    return image

# pick a random index for the plotting example only
oi = np.random.randint(0,X_train.shape[0])

plt.figure(1)
plt.subplot(221)
plt.imshow(X_train[oi])
plt.title('image before transformation')
plt.axis('off')

X_train = norm_image(X_train)
X_valid = norm_image(X_valid)
X_test_original = X_test
X_test = norm_image(X_test)

# plot same image in gray scale
plt.subplot(222)
plt.imshow(X_train[oi].reshape(32,32), cmap = 'gray')
plt.title('image after transformation')
plt.axis('off')
plt.show()
