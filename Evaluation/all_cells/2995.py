df_stats = pd.read_csv(msig.training_stats_filename)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
# span = 111//30 = 3
span = epochs // 100

loss_dict = {
    'loss': df_stats.loss,
    'val_loss': df_stats.val_loss,
    'loss (hw)': reversed_recombined_holt_winters(np.array(df_stats.loss), span=span),
    'val_loss (hw)': reversed_recombined_holt_winters(np.array(df_stats.val_loss), span=span)

}
alphas = {
    'loss': 0.3,
    'val_loss': 0.3,
    'loss (hw)': 1,
    'val_loss (hw)': 1
}

legend_labels = []
for key, value in loss_dict.items():
    ax1.plot(value, alpha=alphas[key])
    legend_labels.append(key)

ax1.set_title(r'timestamps = {}, window_size = {}'.format(msig.n_timestamps, msig.window_size))
ax1.set_xlabel(r'epoch')
ax1.set_xlim((0, len(df_stats.acc)))
ax1.set_ylabel(r'loss')
ax1.set_ylim((0, None))
ax1.grid(True)
ax1.legend(legend_labels)

acc_dict = {
    'acc': df_stats.acc,
    'val_acc': df_stats.val_acc,
    'acc (hw)': reversed_recombined_holt_winters(np.array(df_stats.acc), span=span),
    'val_acc (hw)': reversed_recombined_holt_winters(np.array(df_stats.val_acc), span=span)

}
alphas = {
    'acc': 0.3,
    'val_acc': 0.3,
    'acc (hw)': 1,
    'val_acc (hw)': 1
}

legend_labels = []
for key, value in acc_dict.items():
    ax2.plot(value, alpha=alphas[key])
    legend_labels.append(key)

ax2.set_title(r'neurons = {}, batch_size = {}'.format(n_neurons, batch_size))
ax2.set_xlabel(r'epoch')
ax2.set_xlim((0, len(df_stats.acc)))
ax2.set_ylabel(r'accuracy')
ax2.set_ylim((None, 1))
ax2.grid(True)
ax2.legend(legend_labels)

plt.tight_layout()
plt.savefig(os.path.join(msig.out_dir, 'loss_accuracy.png'))
plt.show()