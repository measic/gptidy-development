import math

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
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
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
    left_lines = []
    right_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), [0, 0, 255], 6)
            if x1 == x2:
                continue
            slope = get_slope(x1, y1, x2, y2)
            if slope < 0:
                if slope > -0.5 or slope < -0.8:
                    continue
                left_lines.append(line)
            elif slope >= 0:
                if slope < 0.5 or slope > 0.8:
                    continue
                right_lines.append(line)
    draw_lines_oneside(img, left_lines, color, thickness)
    draw_lines_oneside(img, right_lines, color, thickness)

def get_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def draw_lines_oneside(img, lines, color, thickness):
    if len(lines) == 0:
        return
    top = 330
    bottom = img.shape[0]
    x1_avg, y1_avg, x2_avg, y2_avg = function_def(lines)
    slope = (y2_avg - y1_avg) / (x2_avg - x1_avg)
    bias = y1_avg - slope * x1_avg
    x1 = (bottom - bias) / slope
    y1 = bottom
    x2 = (top - bias) / slope
    y2 = top
    cv2.line(img, (int(x1), y1), (int(x2), y2), color, thickness)

def function_def(lines):
    lines_size = len(lines)
    x1_sum, y1_sum, x2_sum, y2_sum = (0, 0, 0, 0)
    for line in lines:
        for x1, y1, x2, y2 in line:
            x1_sum += x1
            y1_sum += y1
            x2_sum += x2
            y2_sum += y2
    x1_avg = x1_sum / lines_size
    y1_avg = y1_sum / lines_size
    x2_avg = x2_sum / lines_size
    y2_avg = y2_sum / lines_size
    return (x1_avg, y1_avg, x2_avg, y2_avg)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

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