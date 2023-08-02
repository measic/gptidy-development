variable_def = []
not_pid_importances = []
for feature in feature_names:
    if 'playlist_pid' not in feature:
        variable_def.append(feature)
        idx = feature_names.index(feature)
        not_pid_importances.append(top50importance[idx])