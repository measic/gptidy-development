def function_def(image):
    gray = grayscale(image)
    kernel_size = 5
    blur_gray = gaussian_blur(gray, kernel_size)
    low_threshold = 60
    high_threshold = 100
    edges = canny(blur_gray, low_threshold, high_threshold)
    imshape = image.shape
    vertices = np.array([[(0, imshape[0]), (imshape[1] * 0.48, imshape[0] * 0.6), (imshape[1] * 0.52, imshape[0] * 0.6), (imshape[1], imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)
    rho = 1
    theta = np.pi / 180
    threshold = 90
    min_line_length = 30
    max_line_gap = 30
    line_image = np.copy(image) * 0
    lines = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap, vertices)
    result = weighted_img(lines, image, α=0.8, β=1.0, λ=0.0)
    return result