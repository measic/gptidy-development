# Set up parameters:    
k_size = 9  # Must be an odd number
vertex_ratio_h = .45
vertex_ratio_v = .60
low_thresh = 15
high_thresh = 50
L2gradient = False
rho = 2
theta = 1 * np.pi / 180.
min_votes = 15
min_line_len = 40
max_line_gap = 20
angle = 3 * np.pi / 16
angle_threshold = np.pi / 64

for file in files:
    frame = mpimg.imread('challenge/' + file)
    fig = plt.figure(figsize = (15, 10))
    fig.text(.1, 1, file)
    result = process_image(frame, 
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