i_maxmin = np.argmax(waves_nearest_neighbor, axis=0)
wave_max_distance = np.max(waves_nearest_neighbor, axis=0)
wave_farthest_neighbor_colors = [0] * len(xindex)
wave_farthest_neighbor = np.zeros((len(xindex),))
for i, ii in enumerate(i_maxmin):
    wave_farthest_neighbor_colors[i] = msig.waves[ii].color
    wave_farthest_neighbor[i] = msig.waves[ii].sample_full[i]
transition_vlines = np.where(i_maxmin[1:] - i_maxmin[:-1])[0] + 1
transition_vcolors = [wave_farthest_neighbor_colors[v] for v in transition_vlines]

w_size = 17
center = (w_size - 1) // 2
min_peaks_vlines = []
for i in range(len(xindex) - w_size):
    if np.argmin(wave_max_distance[i:i + w_size]) == center:
        min_peaks_vlines.append(i + center)

min_peaks_vlines = np.array(min_peaks_vlines)
# print(min_peaks_vlines[1:] - min_peaks_vlines[:-1])
# print(min_peaks_vlines)
min_peaks_vcolors = np.array([wave_max_distance[v] for v in min_peaks_vlines])
min_peaks_vcolors /= np.max(min_peaks_vcolors)
# print(len(min_peaks_vcolors))
# print(min_peaks_vcolors)

vmin = 0
vmax = 0.65
cmap = cm.Greys_r

# alphas = np.ones(wave_max_distance.shape) * 0.2
wave_max_distance_colors = Normalize(vmin, vmax, clip=True)(wave_max_distance)
wave_max_distance_colors = cmap(wave_max_distance_colors)
# wave_max_distance_colors[..., -1] = alphas