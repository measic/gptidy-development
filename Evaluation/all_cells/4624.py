image = mpimg.imread('test_images/whiteCarLaneSwitch.jpg')
lane_detected = lane_detection(image)
plt.imshow(lane_detected)