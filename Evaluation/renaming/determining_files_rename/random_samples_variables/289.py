def lane_detection_ppline(image, k_size=3, vertex_ratio_h=0.45, vertex_ratio_v=0.6, low_thresh=50, high_thresh=200, L2gradient=False, rho=2, theta=1 * np.pi / 180.0, min_votes=15, min_line_len=40, max_line_gap=20, angle=3 * np.pi / 16, angle_thresh=np.pi / 16, debug=False):
    """
    Takes an image and parameters and applies the lane detection pipeline.
    Returns an image combining the original and the extended lines detected
    by the algorithm.
     - debug: Whether or not to display the images after each step of the process, for
     debugging or tuning purposes.
    """
    max_y, max_x = image.shape[:2]
    roi = np.array([[(0, max_y), (round(max_x * vertex_ratio_h), round(max_y * vertex_ratio_v)), (round(max_x * (1 - vertex_ratio_h)), round(max_y * vertex_ratio_v)), (max_x, max_y)]])
    if debug:
        plt.subplot(4, 2, 1)
        plt.imshow(image)
    variable_def = grayscale(image)
    if debug:
        plt.subplot(4, 2, 2)
        plt.imshow(variable_def, cmap='gray')
    blur_gray = gaussian_blur(variable_def, k_size)
    if debug:
        plt.subplot(4, 2, 3)
        plt.imshow(blur_gray, cmap='gray')
    edges = canny(blur_gray, low_thresh, high_thresh, L2gradient=L2gradient)
    if debug:
        plt.subplot(4, 2, 4)
        plt.imshow(edges)
    masked_edges = region_of_interest(edges, roi)
    if debug:
        plt.subplot(4, 2, 5)
        plt.imshow(masked_edges)
    line_img, lines = hough_lines(masked_edges, rho, theta, min_votes, min_line_len, max_line_gap)
    if debug:
        plt.subplot(4, 2, 6)
        plt.imshow(line_img)
    try:
        combined = extend_lines(image, lines, angle=angle, angle_thresh=angle_thresh)
        if debug:
            plt.subplot(4, 2, 7)
            plt.imshow(combined)
    except IndexError:
        print('Error. Try relaxing your angle parameters a litte.')
    return combined