def lane_detection(image):
    gray = grayscale(image)
    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = gaussian_blur(gray, 5)

    # Define our parameters for Canny and apply
    low_threshold = 60
    high_threshold = 180
    edges = canny(blur_gray, low_threshold, high_threshold) 

    # This time we are defining a four sided polygon to mask
    imshape = image.shape
    # print('This image is:', type(image), 'with dimensions:', image.shape)
    vertices = np.array([[(0,imshape[0]),(450, 320), (490, 320), (imshape[1],imshape[0])]], dtype=np.int32)

    masked_edges = region_of_interest(edges, vertices)

    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15     # minimum number of votes (intersections in Hough grid cell)
    min_line_len = 40 #minimum number of pixels making up a line
    max_line_gap = 20    # maximum gap in pixels between connectable line segments

    # Run Hough on edge detected image
    # Here the returned image already has the lane line drawn (not in segments)
    line_image = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)

    # Create a "color" binary image to combine with line image
    color_edges = np.dstack((edges, edges, edges)) 

    # Draw the lines on the edge image
    lines_edges = weighted_img(line_image, image, α=0.8, β=1., λ=0.)
    # plt.imshow(lines_edges)
    return lines_edges