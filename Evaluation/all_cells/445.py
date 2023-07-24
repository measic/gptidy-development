dataset = merged.append(negative_samples[merged.columns]).sort_values(by=['playlist_pid']).reset_index(drop=True)
dataset.loc[:,'playlist_pid'] = dataset.playlist_pid.astype(str)
dataset = dataset[list(tracks_df.columns)+['track_uri']+list(playlist_df.columns)+['match']]