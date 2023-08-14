%%time
inference_2 = ed.Gibbs({pi_ed2: qpi_2, mu_ed2: qmu_2, sigmasq_ed2: qsigma_2, z_ed2: qz_2}, data={x_ed2: X})
inference_2.initialize(n_print=500, logdir='log/IMG={}_K={}_T={}_model2'.format(img_no, K, T))
sess = ed.get_session()
tf.global_variables_initializer().run()
for _ in range(inference_2.n_iter):
    info_dict_2 = inference_2.update()
    inference_2.print_progress(info_dict_2)
inference_2.finalize()