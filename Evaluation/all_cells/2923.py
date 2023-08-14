####### Defining network #######
# input: state x
# output: control u

input_layer = tf.placeholder(tf.float32, (None,2), name='in_layer')
fc1 = tf.layers.dense(inputs=input_layer, units=1, activation=tf.nn.tanh, name='fc1', reuse=tf.AUTO_REUSE)
u = tf.layers.dense(inputs=fc1, units=1, activation=tf.nn.tanh, name='fc_out', reuse=tf.AUTO_REUSE)
# u = tf.layers.dense(inputs=input_layer, units=1, name='u_out_layer', reuse=tf.AUTO_REUSE)

### LOSS FUNCTION ### 
loss = tf.add(tf.matmul(tf.matmul(tf.transpose(x), Q), x), 
              tf.matmul(tf.transpose(u), tf.multiply(R, u)), name='loss')

# xs = tf.identity(x, name='xs')
# us = tf.constant(0, name='us')
xs = x
us = u

# cond = lambda i, x, l, xs, us: i < T

# def body(i, x, l, xs, us):
#     next_i = i+1
#     next_x = tf.add(tf.matmul(A, x), tf.multiply(u,B))
#     next_l = tf.add(l,
#                     tf.add(tf.matmul(tf.matmul(tf.transpose(x), Q), x),
#                            tf.matmul(tf.transpose(u), tf.multiply(R, u))))
#     next_xs = tf.concat(xs, next_x)
#     next_us = tf.concat(us, u)
#     return (next_i, next_x, next_l, next_xs, next_us)

# i, xloss_f, traj_f = tf.while_loop(cond, body, 
#                                    loop_vars=[tf.constant(0), x, loss, xs, us],
#                                    shape_invariants=[tf.TensorShape([1,]), tf.TensorShape([2, 1]), 
#                                                      tf.TensorShape([1,]) , tf.TensorShape([2, None]), 
#                                                      tf.TensorShape([1, None])])
# train = tf.train.GradientDescentOptimizer(0.01).minimize(xloss_f.loss)

for i in range(T):
    # LQR loss 
#     x_term = tf.matmul(tf.matmul(tf.transpose(x), Q), x, name='x_term')
#     u_term = tf.matmul(tf.transpose(u), tf.multiply(R, u), name='u_term')
#     loss = tf.add(loss, tf.add(x_term, u_term), name='loss')  # accumulate loss
    
    # Dynamics: advancing the system dynamics
    Ax = tf.matmul(A, x, name='Ax'+str(i))
    Bu = tf.multiply(u, B, name='Bu'+str(i))  # tf.multiply because u is a scalar
    x = tf.add(Ax, Bu, name='state'+str(i))  # next state vector

    loss = tf.add(loss, tf.add(tf.matmul(tf.matmul(tf.transpose(x), Q), x), tf.matmul(tf.transpose(u), tf.multiply(R, u))), name='loss'+str(i))  # accumulate loss    
    
#     u = tf.layers.dense(inputs=tf.transpose(x), units=1, name='u_out_layer', reuse=True)
    
    fc1 = tf.layers.dense(inputs=tf.transpose(x), units=1, name='fc1', reuse=True)
    u = tf.layers.dense(inputs=fc1, units=1, name='fc_out', reuse=True)
    
    xs = tf.concat([xs, x], 1)
    us = tf.concat([us, u], 1)
    
opt = tf.train.GradientDescentOptimizer(0.0001)
train = opt.minimize(loss)
grads_and_vars = opt.compute_gradients(loss)