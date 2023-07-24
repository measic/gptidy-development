image = mpimg.imread('test_images/solidYellowCurve2.jpg')
lane_detected = lane_detection(image)
plt.imshow(lane_detected)