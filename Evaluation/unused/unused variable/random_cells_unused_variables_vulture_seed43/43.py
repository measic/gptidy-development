# Code specific to window_type == sliding

# j = 10
# s0 = slice(0, j)
# s1 = slice(-j, -1)
# s0 = s1
# print(y_hat[s0, s1])
# print(y_true[s0, s1])
# print(y_true_value[s0, s1])
# print(y_pred[s0, s1])
# print(y_pred_value[s0, s1])
# print(y_penalty[s0, s1])
# print(y_score[s0, s1])
# print(np.min(y_score), np.max(y_score))

if msig.sequence_type == 'many2many':
    y_score_mean = y_score.sum(axis=1) / y_score.shape[1]
    y_score_unshifted = np.zeros((msig.n_timestamps, msig.window_size))
    for i in range(msig.window_size):
        y_score_unshifted[i:i + msig.n_samples, i] = y_score[:, i]
    y_score_unshifted_clipped = y_score_unshifted[msig.window_size-1:]
    y_score_unshifted_clipped_mean = y_score_unshifted_clipped.sum(axis=1) / y_score.shape[1]
else:
    y_score_mean = y_score.sum(axis=1) / y_score.shape[1]
    y_score_unshifted = np.zeros((msig.n_timestamps, msig.window_size))
    for i in range(msig.window_size):
        y_score_unshifted[i:i + msig.n_samples, i] = y_score[:, i]
    y_score_unshifted_clipped = y_score_unshifted[msig.window_size-1:]
    y_score_unshifted_clipped_mean = y_score_unshifted_clipped.sum(axis=1) / y_score.shape[1]