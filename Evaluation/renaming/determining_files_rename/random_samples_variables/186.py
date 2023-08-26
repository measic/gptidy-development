X_test_refined = pd.DataFrame([])
r_precisions = []
pbar = tqdm(data_test.groupby(['playlist_pid']))
for pid, df in pbar:
    p_info = df[playlist_df.columns].iloc[0]
    labels = y_test.loc[df.index]
    positive_tracks_idx = labels[labels == 1].index
    variable_def = data_test.loc[positive_tracks_idx]
    sp_positive_tracks = vectorizer.transform(variable_def.values)
    negative_tracks_idx = ~np.isin(data_test.index, positive_tracks_idx)
    negative_tracks = data_test[negative_tracks_idx].drop(playlist_df.columns, axis=1)
    negative_playlist = np.array([p_info.values] * len(negative_tracks))
    negative_playlist_samples = np.hstack([negative_tracks, negative_playlist])
    sp_negative_tracks = vectorizer.transform(negative_playlist_samples)
    test_tracks = vstack([sp_negative_tracks, sp_positive_tracks])
    index_order = negative_tracks.index.append(positive_tracks_idx)
    y_prob = AdaModel.predict_proba(test_tracks)
    y_pred = np.argsort(-y_prob[:, 1])
    best_pred = index_order[y_pred]
    if len(positive_tracks_idx) > 0:
        r_precisions.append(r_precision(positive_tracks_idx, best_pred))
    pbar.set_description('{}'.format(np.mean(r_precisions)))