## Create a dataframe playlist with songs of your choice
## This code might need a little tweaking, I tried not to spend much time on it,
## but it will add a new playlist to the end of merged.

## Will need to be fixed so that new playlist appended gets negative samples now that merged is 
## created after negative samples.

## As you can see below, we can look at the end of merged and see that a new playlist pid has been 
## added and columns are filled in.  The function is going to get the songs from merged.  If the
## songs are not in merged, it's not going to work.  Might be better to use track_uri's instead.

songs1 = ["The Wolves", "Coffee", "Song For You", "Heart Of Gold",
         "Typical Situation", "Ants Marching", "Uncatena"]

def create_my_playlist(songs: list, name, description):
    my_playlist = pd.DataFrame()
    for song in songs:
        my_playlist = my_playlist.append(merged.loc[merged.track_name == song].iloc[0][tracks_df.columns.append(pd.Index(["track_uri"]))])
    playlist_info = pd.DataFrame(columns = list(playlist_df.columns))
    playlist_info["playlist_collaborative"] = pd.Series("false")
    playlist_info["playlist_description"] = description
    playlist_info["playlist_modified_at"] = 1496793600
    playlist_info["playlist_name"] = name
    playlist_info["playlist_num_edits"] = 1
    playlist_info["playlist_num_followers"] = 1
    playlist_info["playlist_pid"] = np.max(merged.playlist_pid) + 1
    playlist_info["playlist_num_artists"] = my_playlist["track_artist_uri"].nunique()
    playlist_info["playlist_num_tracks"] = len(my_playlist)
    playlist_info["playlist_duration_ms"] = np.sum(my_playlist["track_duration_ms"])
    playlist_info["playlist_num_albums"] = my_playlist["track_album_uri"].nunique()
    playlist_info = pd.concat([playlist_info] * len(songs))
    playlist_info.index = list(my_playlist.index)
    result_df =  pd.concat([my_playlist, playlist_info], axis=1)
    result_df.index = range(len(merged), len(merged) + len(songs))
    return result_df

#Try function, and check end of merged, for example
my_playlist = create_my_playlist(songs1, "indie", "indie rock upbeat")
merged = merged.append(my_playlist)
merged.iloc[-30:]