# Use for reading 40,000 playlist csv
###################################################################

dataset.drop(columns = ["playlist_description_frequency", "playlist_name_frequency"])

#These features need to be converted to strings after loading from csv file
to_str_features = ["playlist_pid", "track_artist_name", "track_name", 
                   "track_album_name", "playlist_description", "playlist_name"]

#Convert features to string type after loading csv
for feature in to_str_features:
    dataset[feature] = dataset.[feature].astype(str)