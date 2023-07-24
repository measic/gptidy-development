# The season field in the summary data corresponds to the starting year of the season (e.g. 2000 for 2000-2001 season)
summary_data = file_utils.read_summary_team_data(summary_team_file)
teams = file_utils.read_team_meta_data(team_meta_data_file)
summary_data.head()