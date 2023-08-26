k_size = 3
vertex_ratio_h = 0.45
vertex_ratio_v = 0.6
low_thresh = 50
high_thresh = 200
L2gradient = False
rho = 2
theta = 1 * np.pi / 180.0
min_votes = 15
min_line_len = 40
max_line_gap = 20
variable_def = 3 * np.pi / 16
angle_threshold = np.pi / 16

def process_image(image):
    result = lane_detection_ppline(image, k_size=k_size, low_thresh=low_thresh, high_thresh=high_thresh, L2gradient=L2gradient, rho=rho, theta=theta, min_votes=min_votes, min_line_len=min_line_len, max_line_gap=max_line_gap, angle=variable_def, angle_thresh=angle_threshold, debug=False)
    return result