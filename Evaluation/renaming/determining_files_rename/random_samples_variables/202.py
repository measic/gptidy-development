image = mpimg.imread('test_images/solidWhiteCurve.jpg')
variable_def = lane_detection(image)
plt.imshow(variable_def)