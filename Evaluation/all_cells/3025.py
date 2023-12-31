t_min_max = (msig.timestamps[0], msig.timestamps[-1])
x_test, y_test = msig.generate()
score = model.evaluate(x_test, y_test, batch_size=batch_size)
model.reset_states()
y_hat = model.predict(x_test, batch_size=batch_size)
model.reset_states()
y_pred = np.argmax(y_hat, axis=1)
# y_pred_colors = [msig.waves[i].color for i in msig.labels[msig.window_size-1:]]
y_pred_colors = np.hstack([msig.waves[i].color for i in y_pred])

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 3))
ax.plot(msig.timestamps, msig.mixed_signal, color='grey', alpha=0.3)
ax.scatter(msig.timestamps[msig.window_size-1:], x_test[:, -1, 0], marker='.', c=y_pred_colors)
ax.set_title('loss = {:<6.4f}, accuracy = {:<6.4f}'.format(*score))
ax.set_xlabel('time')
ax.set_xlim(t_min_max)
plt.grid(True)
plt.savefig(os.path.join(msig.out_dir, 'eval_pred.png'))
plt.show()