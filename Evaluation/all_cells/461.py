#Check for relevant features besides playlist_pid numbers
not_pid_features = []
not_pid_importances = []
for feature in feature_names:
    if "playlist_pid" not in feature:
        not_pid_features.append(feature)
        idx = feature_names.index(feature)
        not_pid_importances.append(top50importance[idx])