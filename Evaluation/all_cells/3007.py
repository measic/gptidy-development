nrows = 6
fig, ax = plt.subplots(nrows=nrows, ncols=1, figsize=(15, 3*nrows))

for i, wave in enumerate(msig.waves):
    ax[0].plot(
        xindex,
        waves_nearest_neighbor[i], 
        c=wave.color)
ax[0].set_xlim((xmin, xmax))
ax[0].set_ylim((0, None))
ax[0].grid(True)

for i, wave in enumerate(msig.waves):
    ax[1].plot(
        xindex[wave.indices],
        waves_nearest_neighbor[i, wave.indices], 
        marker='.', 
        c=wave.color)
ax[1].set_xlim((xmin, xmax))
# ax[1].set_xticks([])
ax[1].set_ylim((0, None))
ax[1].grid(True)

ax[2].vlines(xindex, 0, 1, transform=ax[2].get_xaxis_transform(), colors=wave_max_distance_colors)
ax[2].scatter(
    xindex,
    wave_max_distance, 
    marker='.', 
    c=wave_farthest_neighbor_colors,
    zorder=2)
ax[2].set_xlim((xmin, xmax))
ax[2].set_xticks([])
ax[2].set_ylim((0, None))
ax[2].grid(True)

for wave in msig.waves:
    ax[3].plot(
        xindex,
        wave.sample_full, 
        color=wave.color, 
        lw=3)
ax[3].vlines(min_peaks_vlines, 0, 1, transform=ax[3].get_xaxis_transform(), colors=cmap(min_peaks_vcolors))
# ax[3].vlines(xindex, 0, 1, transform=ax[3].get_xaxis_transform(), colors=wave_max_distance_colors)
ax[3].set_xlim((xmin, xmax))
ax[3].set_xticks([])
ax[3].grid(True)

for wave in msig.waves:
    ax[4].plot(
        xindex,
        wave.sample_full, 
        color=wave.color)
ax[4].scatter(
    xindex, 
    wave_farthest_neighbor, 
    marker='o', 
    c=wave_farthest_neighbor_colors)
ax[4].set_xlim((xmin, xmax))
# ax[4].set_xticks([])
ax[4].grid(True)

ax[5].scatter(
    xindex, 
    wave_farthest_neighbor, 
    marker='.', 
    c=wave_farthest_neighbor_colors)
ax[5].vlines(transition_vlines, 0, 1, transform=ax[5].get_xaxis_transform(), colors=transition_vcolors)
ax[5].set_xlim((xmin, xmax))
ax[5].grid(True)

plt.tight_layout()
plt.savefig(os.path.join(msig.out_dir, 'farthest_neighbor_analysis.png'), bbox_inches='tight')