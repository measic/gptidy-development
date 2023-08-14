# Defines preprocessing action and resulting intermediary artifacts
#TODO: double check syntax
data_x = ex.artifact('data_clean_X.json', 'intermediate_X', utag="first")
data_y = ex.artifact('data_clean_y.json', 'intermediate_y', utag="first")