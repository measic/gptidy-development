files = os.listdir('challenge/')
k_size = 7
vertex_ratio_h = 0.45
vertex_ratio_v = 0.6
low_thresh = 60
high_thresh = 100
L2gradient = False
rho = 2
theta = 1 * np.pi / 180.0
min_votes = 15
min_line_len = 20
max_line_gap = 20
angle = 3 * np.pi / 16
angle_thresh = np.pi / 8
debug = True
for file in files:
    frame = mpimg.imread('challenge/' + file)
    fig = plt.figure(figsize=(15, 10))
    fig.text(0.1, 1, file)
    variable_def = process_image_3_channels(frame, k_size=k_size, low_thresh=low_thresh, high_thresh=high_thresh, L2gradient=L2gradient, rho=rho, theta=theta, min_votes=min_votes, min_line_len=min_line_len, max_line_gap=max_line_gap, angle=angle, angle_thresh=angle_threshold, debug=debug)