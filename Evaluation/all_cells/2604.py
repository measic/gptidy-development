%%time
inference = ed.Gibbs({pi_ed: qpi, mu_ed: qmu, sigmasq_ed: qsigma, z_ed: qz},data={x_ed: X})
inference.initialize(n_print=500, logdir='log/IMG={}_K={}_T={}'.format(img_no, K, T))
sess = ed.get_session()
tf.global_variables_initializer().run()
for _ in range(inference.n_iter):
    info_dict = inference.update()
    inference.print_progress(info_dict)
inference.finalize()