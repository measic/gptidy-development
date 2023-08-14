image = mpimg.imread('test_images/solidYellowCurve.jpg')
lane_detected = lane_detection(image)
plt.imshow(lane_detected)