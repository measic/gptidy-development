def function_def(img):
    """ 
    Takes an RGB image and converts it to HLS.
    Returns the converted image (3 channels)
    """
    hls_image = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    return hls_image

def merge_channels(images):
    """
    Merge images from three different channels
     - images: a list of 3 images, each in a channel
    """
    merged = weighted_img(images[0], images[1], α=0.5, β=0.5, λ=0.0)
    merged = weighted_img(merged, images[2], α=1.0, β=0.5, λ=0.0)
    return merged

def lane_detection_ppline_3_channels(image, k_size=3, vertex_ratio_h=0.45, vertex_ratio_v=0.6, low_thresh=50, high_thresh=200, L2gradient=False, rho=2, theta=1 * np.pi / 180.0, min_votes=15, min_line_len=40, max_line_gap=20, angle=3 * np.pi / 16, angle_thresh=np.pi / 16, debug=False):
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
        plt.subplot(5, 3, 1)
        plt.imshow(image)
    blur = gaussian_blur(image, k_size)
    if debug:
        plt.subplot(5, 3, 2)
        plt.imshow(blur)
    hls = function_def(blur)
    if debug:
        plt.subplot(5, 3, 3)
        plt.imshow(hls)
    edges_list = []
    for chan in range(0, 3):
        edges_list.append(canny(hls[:, :, chan], low_thresh, high_thresh, L2gradient=L2gradient))
        if debug:
            plt.subplot(5, 3, chan + 4)
            plt.imshow(edges_list[chan])
    masked_edges_list = []
    for chan in range(0, 3):
        masked_edges_list.append(region_of_interest(edges_list[chan], roi))
        if debug:
            plt.subplot(5, 3, chan + 7)
            plt.imshow(masked_edges_list[chan])
    lines_list = []
    for chan in range(0, 3):
        lines_list.append(hough_lines(masked_edges_list[chan], rho, theta, min_votes, min_line_len, max_line_gap))
        if debug:
            plt.subplot(5, 3, chan + 10)
            plt.imshow(lines_list[chan][0])
    lines = np.zeros((1, 1, 4))
    for chan in range(0, 3):
        lines = np.concatenate((lines, lines_list[chan][1]), axis=0)
    if debug:
        hls_lines_image = merge_channels([lines_list[0][0], lines_list[1][0], lines_list[2][0]])
        plt.subplot(5, 3, 13)
        plt.imshow(hls_lines_image)
    try:
        combined = extend_lines(image, lines, angle=angle, angle_thresh=angle_thresh)
        if debug:
            plt.subplot(5, 3, 14)
            plt.imshow(combined)
    except IndexError:
        print('Error. Try relaxing your angle parameters a litte.')
    return combined

def process_image_3_channels(image, k_size=3, vertex_ratio_h=0.45, vertex_ratio_v=0.6, low_thresh=50, high_thresh=200, L2gradient=False, rho=2, theta=1 * np.pi / 180.0, min_votes=15, min_line_len=40, max_line_gap=20, angle=3 * np.pi / 16, angle_thresh=np.pi / 16, debug=False):
    result = lane_detection_ppline_3_channels(image, k_size=k_size, low_thresh=low_thresh, high_thresh=high_thresh, L2gradient=L2gradient, rho=rho, theta=theta, min_votes=min_votes, min_line_len=min_line_len, max_line_gap=max_line_gap, angle=angle, angle_thresh=angle_threshold, debug=debug)
    return result