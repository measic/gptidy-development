def process_image(image):
    # 1. grayscale
    gray = grayscale(image)

    # 2. Blur
    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = gaussian_blur(gray, kernel_size)

    # 3. Canny edge
    # Define our parameters for Canny and apply
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)


    # 4. Region of interest (4-sided polygon)
    # This time we are defining a four sided polygon to mask
    imshape = image.shape
    xPct = 0.05
    yPct = 0.60

    xbl = imshape[1] * xPct
    xbr = imshape[1] * (1 - xPct)
    xtl = imshape[1] * (0.5 - xPct)
    xtr = imshape[1] * (0.5 + xPct)

    yb = imshape[0]
    yt = imshape[0] * yPct

    vertices = np.array([[(xbl,yb),(xtl, yt), (xtr, yt), (xbr, yb)]],
                        dtype=np.int32)

    masked_image = region_of_interest(edges, vertices)


    # 5. Hough lines
    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15     # minimum number of votes (intersections in Hough grid cell)
    min_line_len = 20 #minimum number of pixels making up a line
    max_line_gap = 30     # maximum gap in pixels between connectable line segments
    
    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    line_img = hough_lines(masked_image, rho, theta, threshold, min_line_len, max_line_gap)


    # 6. Overlay Hough lines with original image
    # Create a "color" binary image to combine with line image
    overlayedImg = weighted_img(line_img, image, 0.8, 1, 0)

    return overlayedImg