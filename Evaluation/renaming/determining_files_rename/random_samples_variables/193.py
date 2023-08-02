def process_image(image):
    gray = grayscale(image)
    kernel_size = 5
    blur_gray = gaussian_blur(gray, kernel_size)
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)
    variable_def = image.shape
    xPct = 0.05
    yPct = 0.6
    xbl = variable_def[1] * xPct
    xbr = variable_def[1] * (1 - xPct)
    xtl = variable_def[1] * (0.5 - xPct)
    xtr = variable_def[1] * (0.5 + xPct)
    yb = variable_def[0]
    yt = variable_def[0] * yPct
    vertices = np.array([[(xbl, yb), (xtl, yt), (xtr, yt), (xbr, yb)]], dtype=np.int32)
    masked_image = region_of_interest(edges, vertices)
    rho = 2
    theta = np.pi / 180
    threshold = 15
    min_line_len = 20
    max_line_gap = 30
    line_img = hough_lines(masked_image, rho, theta, threshold, min_line_len, max_line_gap)
    overlayedImg = weighted_img(line_img, image, 0.8, 1, 0)
    return overlayedImg