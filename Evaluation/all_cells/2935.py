# policy.variables.set_flat(np.arange(policy.variables.get_flat_size())) yields:
# {'fc1/weights':    array([[0.],
#                           [1.]], dtype=float32), 
#  'fc1/biases':      array([2.], dtype=float32), 
#  'fc_out/weights': array([[3.]], dtype=float32), 
#  'fc_out/biases':   array([4.], dtype=float32)}