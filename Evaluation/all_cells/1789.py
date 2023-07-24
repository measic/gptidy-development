other_linear_accuracy = {}
other_deep_accuracy = {}
linear_cv_mats = {}
deep_cv_mats = {}
linear_c_mats = {}
deep_c_mats = {}
linear_v_mats = {}
deep_v_mats = {}
deep_cv_stats = {}
linear_cv_stats = {}
for key in ['c', 'v', 'p', 'm']:
    other_linear_accuracy[key] = np.zeros((len(subjects), 3, 10))
    other_deep_accuracy[key] = np.zeros((len(subjects), 3, 10))
for key in ['sens', 'spec', 'prec', 'f1']:
    deep_cv_stats[key] = np.zeros((len(subjects), 10))
    linear_cv_stats[key] = np.zeros((len(subjects), 10))
for ii, s in enumerate(subjects):
    for style in ['_lin', '']:
        f_string = output.format(s, s, style)
        with open(os.path.join(os.environ['HOME'], f_string), 'rb') as f:
            dicts, dicts2, y_dims, has_data = pickle.load(f, encoding='latin1')
        indices_dicts2, y_hat_dicts2, logits_dicts2 = dicts2
        mats = analysis.indx_dict2conf_mat(indices_dicts2, y_dims)
        c_mat, v_mat, cv_mat = mats
        acc = analysis.conf_mat2accuracy(c_mat, v_mat, cv_mat)
        acc, (cv_sens, cv_spec, cv_prec, cv_f1) = acc
        (c_accuracy, v_accuracy, accuracy_per_cv,
         p_accuracy, m_accuracy) = acc
        cv_mat_r = analysis.indx_dict2reduced_cv_conf_mat(dicts[1],
                                                          list(dicts[1][0].values())[0][0].max()+1)
        if style == '_lin':
            d = other_linear_accuracy
            mat_d = linear_cv_mats
            mat_d_c = linear_c_mats
            mat_d_v = linear_v_mats
            stats_d = linear_cv_stats
        else:
            d = other_deep_accuracy
            mat_d = deep_cv_mats
            mat_d_c = deep_c_mats
            mat_d_v = deep_v_mats
            stats_d = deep_cv_stats
        d['c'][ii, 2] = c_accuracy
        d['v'][ii, 2] = v_accuracy
        d['p'][ii, 2] = p_accuracy
        d['m'][ii, 2] = m_accuracy
        mat_d[s] = cv_mat_r
        mat_d_c[s] = c_mat
        mat_d_v[s] = v_mat
        stats_d['sens'][ii] = cv_sens
        stats_d['spec'][ii] = cv_spec
        stats_d['prec'][ii] = cv_prec
        stats_d['f1'][ii] = cv_f1