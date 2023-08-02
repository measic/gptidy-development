#helper in getting top features and making visual
#convert relevant dataframe columns to lowercase so we can compare with top feature output

track_artist_lower_df = tracks_df["track_artist_uri"].apply(lambda x: x.lower())
track_album_lower_df = tracks_df["track_album_uri"].apply(lambda x: x.lower())
merged_track_uri_lower_df = merged["track_uri"].apply(lambda x: x.lower())

#Take a uri and return album, artist or song title in plain english
def get_translation(uri_type, uri):
    
    track = False  #if a single track/song is input as uri, I need to handle it differently
    if uri_type == "track_artist_uri":
        df = track_artist_lower_df
        col = "track_artist_name"
    elif uri_type == "track_album_uri":
        df = track_album_lower_df
        col = "track_album_name"
    elif uri_type == "track_uri":
        df = merged_track_uri_lower_df
        col = "track_name"
        track = True   #Handle track_name differently by going to the merged df
    for i in range(len(tracks_df)):
        if df[i] == uri:
            if track == True:
                return merged.iloc[i][col]
            return tracks_df.iloc[i][col]
            break