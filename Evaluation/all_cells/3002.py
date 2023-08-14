waves_std = np.std(waves, axis=0)
i_std = np.where(waves_std < 0.32245)[0]

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(15, 6))

ax[0].plot(xindex, waves_std)
ax[0].set_xlim((xmin, xmax))
ax[0].set_xticks([])
ax[0].grid(True)

ax[1].scatter(
    xindex, 
    x_test[0, :, 0], 
    marker='.', 
    c=waves_std)
ax[1].set_xlim((xmin, xmax))
ax[1].grid(True)
plt.tight_layout()
plt.savefig(os.path.join(msig.out_dir, 'std_dev_analysis.png'), bbox_inches='tight')