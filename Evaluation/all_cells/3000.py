waves_nearest_neighbor = []
waves = np.array([w.sample_full for w in msig.waves])
for i, wi in enumerate(msig.waves):
    waves_diff_all = np.abs(wi.sample_full - waves)
    waves_diff = np.delete(waves_diff_all, i, axis=0)
    waves_nearest_neighbor.append(np.min(waves_diff, axis=0))
waves_nearest_neighbor = np.vstack(waves_nearest_neighbor)
print(waves_nearest_neighbor.shape)