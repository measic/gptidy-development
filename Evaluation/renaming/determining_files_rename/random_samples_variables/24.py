if msig.sequence_type == 'many2many':
    variable_def = y_score.sum(axis=1) / y_score.shape[1]
    y_score_unshifted = np.zeros((msig.n_timestamps, msig.window_size))
    for i in range(msig.window_size):
        y_score_unshifted[i:i + msig.n_samples, i] = y_score[:, i]
    y_score_unshifted_clipped = y_score_unshifted[msig.window_size - 1:]
    y_score_unshifted_clipped_mean = y_score_unshifted_clipped.sum(axis=1) / y_score.shape[1]
else:
    variable_def = y_score.sum(axis=1) / y_score.shape[1]
    y_score_unshifted = np.zeros((msig.n_timestamps, msig.window_size))
    for i in range(msig.window_size):
        y_score_unshifted[i:i + msig.n_samples, i] = y_score[:, i]
    y_score_unshifted_clipped = y_score_unshifted[msig.window_size - 1:]
    y_score_unshifted_clipped_mean = y_score_unshifted_clipped.sum(axis=1) / y_score.shape[1]