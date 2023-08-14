# Code specific to window_type == sliding

xmin = 0
xmax = y_score.shape[0]
xindex = range(xmin, xmax)

fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(10, 16))
# ax = plt.Axes(fig, [0., 0., 1., 1.])
# ax.set_axis_off()
# fig.add_axes(ax)

ax[0].scatter(
    xindex, 
    x_test_clipped, 
    marker='.', 
    c=y_true_colors)
ax[0].set_title('epoch = {}'.format(epoch))
ax[0].set_xlim((xmin, xmax))
ax[0].set_xticks([])
ax[0].grid(True)

ax[1].imshow(
    y_score.T, 
    interpolation='nearest', 
    cmap=plt.get_cmap('Spectral'), 
    origin='upper');
ax[1].spines['top'].set_visible(False)
ax[1].set_xlim((xmin, xmax))
ax[1].set_xticks([])
ax[1].set_ylim((y_score.shape[1], 0))
ax[1].set_yticks([y_score.shape[1]])

divider = make_axes_locatable(ax[1])
ax1Top = divider.append_axes("top", 0.5, sharex=ax[1])
ax1Top.xaxis.set_tick_params(labelbottom=False)
ax1Top.plot(y_score_mean)
ax1Top.set_title('sequence model type = {}'.format(msig.sequence_type))
ax1Top.set_xlim((xmin, xmax))
ax1Top.set_ylim((-1, 1))
ax1Top.set_yticks((-1, 0, 1))
ax1Top.grid(True)

ax[2].imshow(
    y_score_unshifted_clipped.T, 
    interpolation='nearest', 
    cmap=plt.get_cmap('Spectral'), 
    origin='upper');
ax[2].spines['top'].set_visible(False)
ax[2].set_xlim((xmin, xmax))
ax[2].set_xticks([])
ax[2].set_ylim((y_score_unshifted_clipped.shape[1], 0))
ax[2].set_yticks([y_score_unshifted_clipped.shape[1]])

divider = make_axes_locatable(ax[2])
ax2Top = divider.append_axes("top", 0.5, sharex=ax[2])
ax2Top.xaxis.set_tick_params(labelbottom=False)
ax2Top.plot(y_score_unshifted_clipped_mean)
ax2Top.set_title('{} window size = {}'.format(window_type, msig.window_size))
ax2Top.set_xlim((xmin, xmax))
ax2Top.set_ylim((-1, 1))
ax2Top.set_yticks((-1, 0, 1))
ax2Top.grid(True)

ax[3].scatter(
    xindex, 
    x_test_clipped,
    marker='.', 
    c=y_pred_colors)
ax[3].set_title('loss = {:<6.4f}, accuracy = {:<.2%}'.format(*score))
ax[3].set_xlim((xmin, xmax))
ax[3].grid(True)

# plt.draw()
plt.savefig(os.path.join(msig.out_dir, 'prediction_analysis.png'), bbox_inches='tight', pad_inches=0.08)
# plt.show()