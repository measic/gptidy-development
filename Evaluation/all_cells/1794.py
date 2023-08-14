for deep in [True, False]:
    for ii, s in enumerate(subjects):
        string = '{}, {}  '.format(subject_labels[s], 'deep' if deep else 'logistic')
        if deep:
            data = deep_all[1.][ii, 2]
        else:
            data = linear_all[1.][ii, 2]
        string = string + '&{} $\pm$ {}\%  '.format(np.around(100*data.mean(), 1),
                                                np.around(100*data.std(), 1))
        for key in ['sens', 'spec', 'prec', 'f1']:
            if deep:
                data = deep_cv_stats[key][ii]
            else:
                data = linear_cv_stats[key][ii]
            string = string + '&{} $\pm$ {}\%  '.format(np.around(100*data.mean(), 1),
                                                    np.around(100*data.std(), 1))
        string = string + ' \\\\'
        print(string)
    string = '{}, {}  '.format('Subj. average', 'deep' if deep else 'logistic')
    if deep:
        data = deep_all[1.][:, 2]
    else:
        data = linear_all[1.][:, 2]
    string = string + '&{} $\pm$ {}\%  '.format(np.around(100*data.mean(), 1),
                                            np.around(100*data.std(), 1))
    for key in ['sens', 'spec', 'prec', 'f1']:
        if deep:
            data = deep_cv_stats[key]
        else:
            data = linear_cv_stats[key]
        string = string + '&{} $\pm$ {}\%  '.format(np.around(100*data.mean(), 1),
                                                np.around(100*data.std(), 1))
    string = string + ' \\\\'
    print(string)
    print()