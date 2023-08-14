track_artist_lower_df = tracks_df['track_artist_uri'].apply(lambda x: x.lower())
track_album_lower_df = tracks_df['track_album_uri'].apply(lambda x: x.lower())
merged_track_uri_lower_df = merged['track_uri'].apply(lambda x: x.lower())

def get_translation(uri_type, uri):
    track = False
    if uri_type == 'track_artist_uri':
        variable_def = track_artist_lower_df
        col = 'track_artist_name'
    elif uri_type == 'track_album_uri':
        variable_def = track_album_lower_df
        col = 'track_album_name'
    elif uri_type == 'track_uri':
        variable_def = merged_track_uri_lower_df
        col = 'track_name'
        track = True
    for i in range(len(tracks_df)):
        if variable_def[i] == uri:
            if track == True:
                return merged.iloc[i][col]
            return tracks_df.iloc[i][col]
            break