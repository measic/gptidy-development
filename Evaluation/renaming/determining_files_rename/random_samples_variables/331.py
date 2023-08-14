X_test_refined = pd.DataFrame([])
r_precisions = []
pbar = tqdm(data_test.groupby(['playlist_pid']))
for pid, df in pbar:
    labels = y_test.loc[df.index]
    from IPython.core.debugger import set_trace
    set_trace()
    targets = dataset.loc[labels.index].track_duration_ms
    positive_targets = dataset.loc[labels[labels == 1].index].index
    variable_def = dataset.loc[X_test[X_test.playlist_pid != pid].index].track_duration_ms
    new_df = df.drop('track_duration_ms', axis=1)
    new_test = variable_def.append(targets)
    new_df = pd.concat([new_df.head(1)] * len(new_test))
    test_playlist_tracks = pd.concat([new_df.reset_index(drop=True), new_test.reset_index(drop=True)], axis=1).set_index(new_test.index)
    test_playlist_tracks = (test_playlist_tracks - test_playlist_tracks.mean()) / (test_playlist_tracks.std() + 1e-08)
    X_test_refined = X_test_refined.append(test_playlist_tracks)
    y_prob = pd.DataFrame(lr_clf.predict_proba(test_playlist_tracks), index=test_playlist_tracks.index)
    y_prob = y_prob.sort_values(by=[1], ascending=False)
    if len(positive_targets) > 0:
        r_precisions.append(r_precision(positive_targets, y_prob.index))
    pbar.set_description('{}'.format(np.mean(r_precisions)))