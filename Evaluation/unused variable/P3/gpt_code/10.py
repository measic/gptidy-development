import math

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
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

''' Calculate filtered results '''
def filterFn(alpha, prev, new):
    return alpha * new + (1 - alpha) * prev

''' Clear global previous between videos '''
def clearUnjitter():
    global previous
    previous = {
        "right": [0, 0, 0, 0], # x1, y1, x2, y2
        "left": [0, 0, 0, 0]
    }

'''
Unjitter it as tipped by Vivek Jadav in the following topic:
https://carnd-forums.udacity.com/display/CAR/questions/22086201/p1-how-to-avoid-jittery-lines
'''
def unjitter(side, value):
    global previous
    alpha = 0.6
    # destructure value
    x1 = value[0]
    y1 = value[1]
    x2 = value[2]
    y2 = value[3]
    # set start value on first frame
    if previous[side][0] == 0:
        previous[side][0] = x1
    if previous[side][1] == 0:
        previous[side][1] = y1
    if previous[side][2] == 0:
        previous[side][2] = x2
    if previous[side][3] == 0:
        previous[side][3] = y2
    # calculate filtered results
    x1 = filterFn(alpha, previous[side][0], x1)
    y1 = filterFn(alpha, previous[side][1], y1)
    x2 = filterFn(alpha, previous[side][2], x2)
    y2 = filterFn(alpha, previous[side][3], y2)
    # set new values to previous
    previous[side][0] = x1
    previous[side][1] = y1
    previous[side][2] = x2
    previous[side][3] = y2
    return [x1, y1, x2, y2]

def draw_lines(img, lines, color=[255, 0, 0], thickness=5):
    global previous
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
    sides = {
        "left": [],
        "right": []
    }
    yMin = img.shape[0]
    xHalf = img.shape[1] / 2
    yMax = 315
    if lines != None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                slope = ((y2 - y1) / (x2 - x1))
                if slope > 0.50 and slope < 0.8: # Right line, because of positive slope (y-reversed)
                    sides["right"].append([x1,y1,x2,y2]) 
                elif slope < -0.50 and slope > -0.8: # Left line because of negative slope
                    sides["left"].append([x1,y1,x2,y2])
    yHalf = None
    for side in sides:
        avgSlope = None
        totalSlope = 0
        totalWeight = 0
        xAvg = None
        yAvg = None
        for x1,y1,x2,y2 in sides[side]:
            slope = (y2 - y1) / (x2 - x1)
            length = math.sqrt(abs(x2-x1)^2+abs(y2 - y1)^2)
            if xAvg == None:
                #avgSlope = slope
                xAvg = (x1 + x2) / 2
                yAvg = (y1 + y2) / 2
            else:
                #avgSlope = (avgSlope + slope) / 2
                xAvg = (xAvg + ((x1 + x2) / 2)) / 2
                yAvg = (yAvg + ((y1 + y2) / 2)) / 2
            totalSlope += slope * length
            totalWeight += length
        if totalWeight > 0:
            avgSlope = totalSlope / totalWeight
        if avgSlope != None and xAvg != None and yAvg != None:
            yIntercept = -(avgSlope * xAvg) + yAvg
            xMax = (yMax - yIntercept) / avgSlope
            xMin = (yMin - yIntercept) / avgSlope
            if side == "right":
                offset = 20
            else:
                offset = -20
            _yHalf = avgSlope * (xHalf + offset) + yIntercept 
            if yHalf == None:
                yHalf = _yHalf
            else:
                xHalf