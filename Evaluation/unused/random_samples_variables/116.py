with tf.Session() as sess:
    A_np, B_np, Q_np, R_np = sess.run([A, B, Q, R])

K, P, eig = controlpy.synthesis.controller_lqr_discrete_time(A_np, B_np, Q_np, R_np)
x_np = x0
u_np = (-K@x_np)
xs_np, us_np = np.array(x_np), np.array(u_np)
loss_np = 0
for i in range(T):
    loss_np += x_np.T@Q_np@x_np + u_np.T*R_np*u_np
    x_np = A_np@x_np + B_np@u_np
    u_np = (-K@x_np)
    xs_np = np.hstack([xs_np, x_np])
    us_np = np.hstack([us_np, u_np])