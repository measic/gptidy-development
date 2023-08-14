variable_def = 'test_images_output'
if not os.path.exists(variable_def):
    os.makedirs(variable_def)
image = mpimg.imread('test_images/solidYellowLeft.jpg')
print('This image is:', type(image), 'with dimensions:', image.shape)
plt.imshow(image)