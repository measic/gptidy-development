x_test, y_test = msig.generate(sequence_code='1tf_1tc')
epoch = 0
score = model.evaluate(x_test, y_test, batch_size=batch_size)
# if stateful:
#     model.reset_states()
y_hat = model.predict(x_test, batch_size=batch_size)
# if stateful:
#     model.reset_states()

# Code specific to window_type == sliding
# ii = 100
# x_test = test_dict['X']
# y_test = test_dict['y']
# score = test_dict['score'][ii]
# epoch = test_dict['epoch'][ii]
# y_hat = test_dict['y_hat'][ii]
# x_test_clipped = x_test[:, test_dict['window_size'] - 1:, 0]

y_true = np.argmax(y_test, axis=-1)
y_pred = np.argmax(y_hat, axis=-1)

y_correct = (y_pred == y_true) * 1
y_fail = (y_pred != y_true) * 1

print('x_test  {}'.format(x_test.shape))
print('y_test  {}'.format(y_test.shape))
print('y_true  {}'.format(y_true.shape))
print(score)
print('y_hat   {}'.format(y_hat.shape))
print('y_pred  {}'.format(y_pred.shape))

print(y_hat[0, :4])
print(y_true[0, :10])
print(y_pred[0, :10])
print(y_fail[0, :10])

i_fail = np.where(y_fail)[1]
print(i_fail.shape)
# print(i_fail)

# y_true_colors = np.hstack([msig.waves[i].color for i in y_true])    
# y_pred_colors = np.hstack([msig.waves[i].color for i in y_pred])
y_true_colors = np.hstack([msig.waves[i].color for i in y_true[0]])
y_pred_colors = np.hstack([msig.waves[i].color for i in y_pred[0]])
# y_true_colors = [msig.waves[i[-1]].color for i in y_true[0]]
# y_pred_colors = [msig.waves[i[-1]].color for i in y_pred[0]]

print('y_pred_colors {}'.format(y_pred_colors.shape))
# print(msig.timestamps.shape)


# Code specific to window_type == sliding

# I derived y_score based on my intuition (i.e. out of thin air).  Would be nice to find some theoretical justification for why this is I like it so much.
# if msig.sequence_type == 'many2many':
#     y_true_value = [y_hat[i, j, y_true[i, j]] for i in range(y_true.shape[0]) for j in range(y_true.shape[1])]
#     y_pred_value = [y_hat[i, j, y_pred[i, j]] for i in range(y_pred.shape[0]) for j in range(y_pred.shape[1])]
#     y_true_value = np.reshape(y_true_value, y_true.shape)
#     y_pred_value = np.reshape(y_pred_value, y_pred.shape)
#     y_penalty = y_true_value - y_pred_value
#     y_score = y_true_value + y_penalty
# else:
#     y_true_value = y_hat[(np.arange(y_true.shape[0]), y_true[0])]
#     y_pred_value = y_hat[(np.arange(y_pred.shape[0]), y_pred[0])]
#     y_penalty = y_true_value - y_pred_value
#     y_score = y_true_value + y_penalty
    # Hack: Make y_score the same shape as many2many y_score
#     y_score = y_score[:, None] * np.ones((msig.window_size,))[None, :]
# print(y_true_value.shape)
# print(y_pred_value.shape)
# print(y_penalty.shape)
# print(y_score.shape)