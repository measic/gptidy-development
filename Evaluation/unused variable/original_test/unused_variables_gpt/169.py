# More thresholds means higher granularity for the area under the curve approximation
# Feel free to experiment with the number of thresholds
num_thresholds = 1000 
thresholds = tf.lin_space(0.0, 1.0, num_thresholds).numpy()