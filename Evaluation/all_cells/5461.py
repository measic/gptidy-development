challenge_output = 'extra.mp4'

# Parameters:

k_size = 7
vertex_ratio_h = .45
vertex_ratio_v = 0.65
low_thresh = 60
high_thresh = 100
L2gradient = False
rho = 2
theta = 1 * np.pi / 180.
min_votes = 15
min_line_len = 20
max_line_gap = 20
angle = 3 * np.pi / 16
angle_thresh = np.pi / 32
debug = True

challenge_clip = clip2.fl_image(lambda x: process_image_3_channels(x,
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
                                                        debug = False))
%time challenge_clip.write_videofile(challenge_output, audio=False)