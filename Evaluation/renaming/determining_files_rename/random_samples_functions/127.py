def function_def(image):
    gray = grayscale(image)
    kernel_size = 5
    blur_gray = gaussian_blur(gray, 5)
    low_threshold = 60
    high_threshold = 180
    edges = canny(blur_gray, low_threshold, high_threshold)
    imshape = image.shape
    vertices = np.array([[(0, imshape[0]), (450, 320), (490, 320), (imshape[1], imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)
    rho = 2
    theta = np.pi / 180
    threshold = 15
    min_line_len = 40
    max_line_gap = 20
    line_image = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)
    color_edges = np.dstack((edges, edges, edges))
    lines_edges = weighted_img(line_image, image, α=0.8, β=1.0, λ=0.0)
    return lines_edges