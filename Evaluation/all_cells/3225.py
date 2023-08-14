X = np.array(bricks).reshape(-1, im_shape[0]*im_shape[1])
X = np.vstack((X, np.array(balls).reshape(-1, im_shape[0]*im_shape[1])))

y = np.zeros(X.shape[0])
y[len(bricks):] = 1.0