if msig.sequence_type == 'many2many':
    y_score_mean = y_score.sum(axis=1) / y_score.shape[1]
    variable_def = np.zeros((msig.n_timestamps, msig.window_size))
    for i in range(msig.window_size):
        variable_def[i:i + msig.n_samples, i] = y_score[:, i]
    y_score_unshifted_clipped = variable_def[msig.window_size - 1:]
    y_score_unshifted_clipped_mean = y_score_unshifted_clipped.sum(axis=1) / y_score.shape[1]
else:
    y_score_mean = y_score.sum(axis=1) / y_score.shape[1]
    variable_def = np.zeros((msig.n_timestamps, msig.window_size))
    for i in range(msig.window_size):
        variable_def[i:i + msig.n_samples, i] = y_score[:, i]
    y_score_unshifted_clipped = variable_def[msig.window_size - 1:]
    y_score_unshifted_clipped_mean = y_score_unshifted_clipped.sum(axis=1) / y_score.shape[1]