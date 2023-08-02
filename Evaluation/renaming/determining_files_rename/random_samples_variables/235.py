import math
leftline = [(0, 0, 0, 0)]
rightline = [(0, 0, 0, 0)]

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        variable_def = (255,) * channel_count
    else:
        variable_def = 255
    cv2.fillPoly(mask, vertices, variable_def)
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

def draw_lines_roi(img, lines, vertices, color=[255, 0, 0], thickness=2):
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
    global leftline
    global rightline
    imshape = img.shape
    y_min = np.int(imshape[0] * 0.61)
    y_max = imshape[0]
    left_x1 = []
    left_x2 = []
    right_x1 = []
    right_x2 = []
    left_count = 0
    right_count = 0
    for line in lines:
        for x1, y1, x2, y2 in line:
            m = (y2 - y1) / (x2 - x1)
            if (m > 0.3) & (m < 7):
                fit = np.polyfit([x1, x2], [y1, y2], 1)
                right_x1.append(np.int(np.float(y_min - fit[1]) / np.float(fit[0])))
                right_x2.append(np.int(np.float(y_max - fit[1]) / np.float(fit[0])))
                right_count += 1
            if (m < -0.3) & (m > -7):
                fit = np.polyfit([x1, x2], [y1, y2], 1)
                left_x1.append(np.int(np.float(y_min - fit[1]) / np.float(fit[0])))
                left_x2.append(np.int(np.float(y_max - fit[1]) / np.float(fit[0])))
                left_count += 1
    if left_count > 0:
        left_line_x1 = np.int(np.nanmedian(left_x1))
        left_line_x2 = np.int(np.nanmedian(left_x2))
        if leftline[0][2] != 0:
            if (abs(leftline[0][2] - left_line_x2) < 100) & (abs(leftline[0][0] - left_line_x1) < 50):
                leftline = [(left_line_x1, y_min, left_line_x2, y_max)]
        else:
            leftline = [(left_line_x1, y_min, left_line_x2, y_max)]
    if right_count > 0:
        right_line_x1 = np.int(np.nanmedian(right_x1))
        right_line_x2 = np.int(np.nanmedian(right_x2))
        if rightline[0][2] != 0:
            if (abs(rightline[0][2] - right_line_x2) < 100) & (abs(rightline[0][0] - right_line_x1) < 50):
                rightline = [(right_line_x1, y_min, right_line_x2, y_max)]
        else:
            rightline = [(right_line_x1, y_min, right_line_x2, y_max)]
    newlines = [leftline, rightline]
    draw_lines(img, newlines, color, thickness)
    return img

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap, vertices):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    result = draw_lines_roi(line_img, lines, vertices, [255, 0, 0], 14)
    return result

def weighted_img(img, initial_img, α=0.8, β=1.0, λ=0.0):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_img` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, λ)