variable_def = mpimg.imread('test_images/solidWhiteCurve.jpg')
lane_detected = lane_detection(variable_def)
plt.imshow(lane_detected)