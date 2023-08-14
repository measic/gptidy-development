label_pickle_path = '../data/amazonas/labels.pkl'
if not os.path.exists(label_pickle_path):
    labels_without_vs = list(labels)
    labels_with_vs = {}
    if is_pangeo_data:
        gcs_get_dir('pangeo-data/gross/ws_mask', 'ws_mask', fs)
    for label in tqdm(labels):
        ds = xr.open_zarr(f'ws_mask/amazonas/{label}')
        da = ds['mask']
        olat, olon = da.attrs['outlet']
        idx = df_ll[(olat-0.25/1200<df_ll.new_lat.values) & (df_ll.new_lat.values<olat+0.25/1200) & (olon-0.25/1200<df_ll.new_lon.values) & (df_ll.new_lon.values<olon+0.25/1200)].index.values
        if len(idx) > 0:
            labels_without_vs.remove(label)
            labels_with_vs[label] = list(df_vs.iloc[idx].station.values)
    with open(label_pickle_path, 'wb') as f:
        pickle.dump((labels_with_vs, labels_without_vs), f)
else:
    with open(label_pickle_path, 'rb') as f:
        labels_with_vs, labels_without_vs = pickle.load(f)