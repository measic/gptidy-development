test_year = 2018

# scale the feature data corresponding to the 2018 tournament
feature_copy = feature_data[feature_data['season_t'] == test_year].copy()

feature_copy.head()