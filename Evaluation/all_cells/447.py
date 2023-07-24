# Include the features in the list below
# features = [
#     'playlist_duration_ms', 'playlist_num_albums', 'playlist_num_artists',
#     'playlist_num_edits', 'playlist_num_followers', 'playlist_num_tracks',
#     'playlist_pid', 'track_duration_ms'
# ]
# data_x = dataset[features]
data_x = dataset.loc[:, dataset.columns != 'match']
data_y = dataset.match
data_train, data_test, y_train, y_test = train_test_split(
    data_x,
    data_y,
    test_size=0.1,
    # stratify=dataset.playlist_pid,
    stratify=dataset[['playlist_pid', 'match']],
    random_state=42,
    shuffle=True)