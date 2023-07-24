game_data = utils.compute_game_data(tourney_data, teams)

# The season year in the computer rankings file correspond to the tournament year (e.g. 2003 for 2002-2003 season)
computer_rankings = pd.read_csv(Path(rankings_data_file))
computer_rankings = computer_rankings[computer_rankings['season'] >= start_tournament]

# Recoding the tourney data to generate team and opp_team fields to replace win and lose fields
# Also add a start season field to the tourney data for merging with summary data
tourney_data = utils.recode_tourney_data(tourney_data)

# Merge the tourney data with the summary data. Handle the discrepancy in the season encodings. 
tourney_data = file_utils.merge_tourney_summary_data(tourney_data, summary_data)

tourney_data = file_utils.join_tourney_team_data(tourney_data, teams)

# Add computer ranking data to team data
tourney_comp_ratings = file_utils.merge_tourney_ranking_data(tourney_data, computer_rankings)
tourney_comp_ratings = utils.implement_top_conference_feature(game_data, tourney_comp_ratings)
tourney_comp_ratings = utils.implement_seed_threshold_feature(tourney_comp_ratings)
tourney_comp_ratings = utils.compute_delta_features(tourney_comp_ratings)

tourney_comp_ratings.dropna(inplace=True)
tourney_comp_ratings[tourney_comp_ratings.isnull().any(axis=1)]
