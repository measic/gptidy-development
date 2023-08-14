image_names = os.listdir("test_images/")
for image_name in image_names:
    print('processing image ' + image_name)
    image = mpimg.imread('test_images/' + image_name)
    lane_detected = lane_detection(image)
    output_path = output_directory + "/" + "lane_detected_" + image_name
    mpimg.imsave(output_path, lane_detected)