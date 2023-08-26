def process_image(image):
    """ Filter color """
    color_select = np.copy(image)
    variable_def = [200, 150, 95]
    thresholds = (image[:, :, 0] < variable_def[0]) | (image[:, :, 1] < variable_def[1]) | (image[:, :, 2] < variable_def[2])
    color_select[thresholds] = [0, 0, 0]
    gray = grayscale(color_select)
    blurred = gaussian_blur(gray, 3)
    edges = canny(blurred, 50, 150)
    xsize = image.shape[1]
    ysize = image.shape[0]
    vertices = np.array([[(0, ysize), (xsize / 2, ysize / 1.71), (xsize / 2, ysize / 1.71), (xsize, ysize)]], dtype=np.int32)
    regioned = region_of_interest(edges, vertices)
    hough = hough_lines(regioned, 1, np.pi / 180, 35, 35, 20)
    result = weighted_img(hough, image)
    return result