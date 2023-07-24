msig.save_config()

t_min_max = (msig.timestamps[0], msig.timestamps[-1])

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 3))
legend_labels = []

for wave in msig.waves:
    ax.plot(wave.timestamps, wave.sample, marker='.', color=wave.color)
    legend_labels.append(wave.name)

ax.set_xlim(t_min_max)
plt.grid(True)
ax.legend(legend_labels)
plt.savefig(os.path.join(msig.out_dir, 'all_waves_with_truth.png'))
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 3))
ax.scatter(msig.timestamps, msig.mixed_signal, color='grey', marker='.', alpha=0.5)
ax.set_xlim(t_min_max)
plt.grid(True)
ax.legend([msig.name], loc='upper right', bbox_to_anchor=(0.99, 0.99))
plt.savefig(os.path.join(msig.out_dir, 'mixed_signal.png'))
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 3))
ax.plot(msig.timestamps, msig.mixed_signal, color='grey', alpha=0.5)
y_test_colors = np.hstack([msig.waves[i].color for i in msig.labels])
ax.scatter(msig.timestamps, msig.mixed_signal, marker='.', c=y_test_colors)
ax.set_xlim(t_min_max)
plt.grid(True)
plt.savefig(os.path.join(msig.out_dir, 'mixed_signal_with_truth.png'))
plt.show()