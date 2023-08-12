# Edward Model
with tf.name_scope("model"):
    pi_ed = Dirichlet(concentration=tf.constant([1.0] * K, name="pi/weights"), name= "pi")
    mu_ed = Normal(loc= tf.ones(D, name="centroids/loc") * 127, 
                scale= tf.ones(D, name="centroids/scale") * 80, sample_shape=K, name= "centroids")
    sigmasq_ed = InverseGamma(concentration=tf.ones(D, name="variability/concentration"), 
                         rate=tf.ones(D, name="variability/rate"), sample_shape=K, name= "variability")
    x_ed = ParamMixture(pi_ed, {'loc': mu_ed, 'scale_diag': tf.sqrt(sigmasq_ed)},
                     MultivariateNormalDiag, sample_shape=N, name= "mixture")
    z_ed = x_ed.cat