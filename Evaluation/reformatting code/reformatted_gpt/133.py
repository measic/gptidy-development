# TODO: Build your pipeline that will draw lane lines on the test_images
# then save them to the test_images directory.

def lane_detection_ppline(image, 
                          k_size=3,
                          vertex_ratio_h=.45,
                          vertex_ratio_v=0.60,
                          low_thresh=50,
                          high_thresh=200,
                          L2gradient=False,
                          rho=2,
                          theta=1 * np.pi / 180.,
                          min_votes=15,
                          min_line_len=40,
                          max_line_gap=20,
                          angle=3 * np.pi / 16,
                          angle_thresh=np.pi / 16,
                          debug=False):
    '''
    Takes an image and parameters and applies the lane detection pipeline.
    Returns an image combining the original and the extended lines detected
    by the algorithm.
    - debug: Whether or not to display the images after each step of the process, for
    debugging or tuning purposes.
    '''
    max_y, max_x = image.shape[:2]  # Grab image dimensions
    # Define 4-sided polygon in relation to image dimensions:
    roi = np.array([[(0, max_y), 
                     (round(max_x * vertex_ratio_h), round(max_y * vertex_ratio_v)),
                     (round(max_x * (1 - vertex_ratio_h)), round(max_y * vertex_ratio_v)),
                     (max_x, max_y)]])
    if debug:
        plt.subplot(4, 2, 1)
        plt.imshow(image)
    
    ## 1. Conversion to grayscale ##
    gray = grayscale(image)
    if debug:
        plt.subplot(4, 2, 2)
        plt.imshow(gray, cmap='gray')

    ## 2. Gaussian smoothing with custom parameters ##
    blur_gray = gaussian_blur(gray, k_size)
    if debug:
        plt.subplot(4, 2, 3)
        plt.imshow(blur_gray, cmap='gray')
    
    ## 3. Canny filter ##
    edges = canny(blur_gray, low_thresh, high_thresh, L2gradient=L2gradient)
    if debug:
        plt.subplot(4, 2, 4)
        plt.imshow(edges)
    
    ## 4. Mask for Region of interest ##
    masked_edges = region_of_interest(edges, roi)
    if debug:
        plt.subplot(4, 2, 5)
        plt.imshow(masked_edges)
    
    ## 5. Hough transform ##
    line_img, lines = hough_lines(masked_edges, rho, theta, min_votes, min_line_len, max_line_gap)
    if debug:
        plt.subplot(4, 2, 6)
        plt.imshow(line_img)
    
    ## 6. Extend lines and create the combined image ##
    try:
        combined = extend_lines(image, lines, angle=angle, angle_thresh=angle_thresh)
        if debug:
            plt.subplot(4, 2, 7)
            plt.imshow(combined)
    except IndexError:
        print('Error. Try relaxing your angle parameters a litte.')
    return combined