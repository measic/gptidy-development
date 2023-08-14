nrows = 2
fig, ax = plt.subplots(nrows=nrows, ncols=1, figsize=(15, 3*nrows))

for i, wave in enumerate(msig.waves):
    ax[0].scatter(
        xindex,
        wave.sample_full, 
        marker='.', 
        c=waves_nearest_neighbor[i]
    )
ax[0].set_xlim((xmin, xmax))
ax[0].set_xticks([])
ax[0].grid(True)

for i, wave in enumerate(msig.waves):
    ax[1].scatter(
        xindex[wave.indices],
        wave.sample, 
        marker='.', 
        c=waves_nearest_neighbor[i, wave.indices]
    )
ax[1].set_xlim((xmin, xmax))
ax[1].grid(True)
plt.tight_layout()
plt.savefig(os.path.join(msig.out_dir, 'nearest_neighbor_analysis.png'), bbox_inches='tight')