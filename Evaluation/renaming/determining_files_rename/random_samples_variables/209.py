xmin = 0
xmax = x_test.shape[1]
xindex = np.arange(xmin, xmax)
variable_def = 3
fig, ax = plt.subplots(nrows=variable_def, ncols=1, figsize=(15, 3 * variable_def))
ax[0].scatter(xindex, x_test[0, :, 0], marker='.', c=y_true_colors)
ax[0].set_title('epoch = {}'.format(epoch))
ax[0].set_xlim((xmin, xmax))
ax[0].set_xticks([])
ax[0].grid(True)
ax[1].scatter(xindex, x_test[0, :, 0], marker='.', c=y_pred_colors)
ax[1].set_title('loss = {:<6.4f}, accuracy = {:<.2%}'.format(*score))
ax[1].set_xlim((xmin, xmax))
ax[1].set_xticks([])
ax[1].grid(True)
legend_labels = []
for wave in msig.waves:
    ax[2].plot(xindex, wave.sample_full, color=wave.color, zorder=1)
    legend_labels.append(wave.name)
ax[2].scatter(xindex[i_fail], x_test[0, i_fail, 0], marker='o', c=y_pred_colors[i_fail], zorder=2)
ax[2].set_xlim((xmin, xmax))
ax[2].grid(True)
ax[2].legend(legend_labels)
plt.tight_layout()
plt.savefig(os.path.join(msig.out_dir, 'prediction_analysis.png'), bbox_inches='tight')