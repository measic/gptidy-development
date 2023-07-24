# The season in the tournamnet data corresponds to the year the tournament occurs (e.g. 2003 for season 2002-2003)
tourney_data = file_utils.read_tournament_results(tournament_data_file,start_tournament)
tourney_data.describe()
