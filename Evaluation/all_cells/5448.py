# Set up parameters:    
k_size = 3
vertex_ratio_h = .45
vertex_ratio_v = .60
low_thresh = 50
high_thresh = 150
L2gradient = False
rho = 2
theta = 1 * np.pi / 180.
min_votes = 15
min_line_len = 40
max_line_gap = 20
angle = 3 * np.pi / 16
angle_threshold = np.pi / 16

subplot_nr = 1
# Loop through files in the test_images directory:
for f in files:
    plt.figure(figsize = (15, 10))
    image = mpimg.imread('test_images/'+ f)

    ## Display original image combined with extended lines:
    
    combined = lane_detection_ppline(image, 
                                     vertex_ratio_h = vertex_ratio_h,
                                     vertex_ratio_v = vertex_ratio_v,
                                     k_size = k_size,
                                     low_thresh = low_thresh,
                                     high_thresh = high_thresh,
                                     L2gradient = L2gradient,
                                     rho = rho,
                                     theta = theta,
                                     min_votes = min_votes,
                                     min_line_len = min_line_len,
                                     max_line_gap = max_line_gap,
                                     angle = angle,
                                     angle_thresh = angle_threshold,
                                     debug = True)  
    plt.imshow(combined)
    subplot_nr += 1