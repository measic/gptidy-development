import math

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def canny(img, low_threshold, high_threshold, L2gradient):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold, L2gradient = L2gradient)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    """
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)


    
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), 
                            minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img, lines

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_img` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, λ) 

def exclude_outliers(data, m = 2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def extend_lines(img, lines, angle = np.pi / 4, angle_thresh = np.pi / 8):
    '''
    Draws extended lines on the original image.
    
    Returns the combined image.
    Args:
    - img: Should be the original image used for lane line detection
    - lines: The second output of hough_lines; a collection of line-end vertices    
    - angle: Approximate angle (in radians) that left lines are expected to form 
    with the horizontal. For right lines, the function uses pi - angle (assumed
    symetry).
    - angle_thresh: Used to filter out lines whose angle to the horizontal is too
    far from either angle or pi - angle. Only left lines (resp. right lines) within 
    angle +/- angle_thresh (resp. pi - angle +/- angle_thresh) are retained. Recommended
    values are pi/8 to pi/20. Extreme values will cause problems.
    '''
    
    left_lines = list()
    right_lines = list()
    middles_left = list()
    middles_right = list()
    slopes_left = list()
    slopes_right = list()
    y_min_left = img.shape[0]
    y_min_right = img.shape[0]
    
     
    ## Collect left and right lines into separate lists based on slope
    for line in lines:  
        slope = (line[0, 3] - line[0, 1]) / (line[0, 2] - line[0, 0])
        # Filter and classify lines as left or right based on their slope:
        if (np.tan(np. pi - angle - angle_thresh)) < slope < (np.tan(np.pi - angle + angle_thresh)):
            left_lines.append(line)  # Add line to our collection of left lines
            slopes_left.append(slope)  # Also collect slopes of left lines
            if min((line[0, 3], line[0, 1])) < y_min_left:
                y_min_left = min((line[0, 3], line[0, 1]))  # and minimum y values of left lanes
        elif (np.tan(angle - angle_thresh)) < slope < (np.tan(angle + angle_thresh)):
            right_lines.append(line)  # Same for right lanes
            slopes_right.append(slope)  # and their slopes
            if min((line[0, 3], line[0, 1])) < y_min_right:
                y_min_right = min((line[0, 3], line[0, 1])) # and their min y values
       
    ## Calculate middle positions of left and right lines
    for line in left_lines:
        middles_left.append(
            (min(line[0, 2], line[0, 0]) + np.abs(line[0, 2] - line[0, 0]) / 2,
             min(line[0, 3], line[0, 1]) + np.abs(line[0, 3] - line[0, 1]) / 2))
    for line in right_lines:
        middles_right.append(
            (min(line[0, 2], line[0, 0]) + np.abs(line[0, 2] - line[0, 0]) / 2,
             min(line[0, 3], line[0, 1]) + np.abs(line[0, 3] - line[0, 1]) / 2))
    
    ## Convert to np.array and calculate medians of middle positions (less sensitive to outliers
    ## than the mean):
    middles_left = np.array(middles_left)
    middles_right = np.array(middles_right)
    median_left = np.zeros(2)
    median_right = np.zeros(2)
    for j in range(2):
        median_left[j] = np.median(middles_left[:, j])
        median_right[j] = np.median(middles_right[:, j])
    
    ## Calculate parameters of the left and right average lines:
    slopes_left = np.array(slopes_left)
    slopes_right = np.array(slopes_right)
    slope_left = np.median(slopes_left)  # Slopes are filtered by value so mean and median are close
    slope_right = np.median(slopes_right)
    intercept_left = median_left[1] - slope_left * median_left[0]
    intercept_right = median_right[1] - slope_right * median_right[0]    
    
    ## Define end vertices of both lines:
    solid_lines = np.array([[
        [0, round(intercept_left), # (x1, y1) for left line
        round((y_min_left - intercept_left) / slope_left), y_min_left]], # (x2, y2) for left line
        [[img.shape[1], round(img.shape[1] * slope_right + intercept_right),  # (x1, y1) for right line
        round((y_min_right - intercept_right) / slope_right), y_min_right  # (x2, y2) for right line
          ]]], np.int32)
    
    ## Create the combined image:
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, solid_lines, color=[255, 0, 0], thickness=10)
    combined_image = weighted_img(line_img, img, α = 1., β= 0.7, λ=0.)

    return combined_image
