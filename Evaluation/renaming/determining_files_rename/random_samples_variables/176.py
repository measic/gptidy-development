variable_def = 1.21
botan_height_m = 1.85
average_adult_human_height_m = 1.688
biggest_distance_m = max(abs(variable_def - average_adult_human_height_m), abs(botan_height_m - average_adult_human_height_m))
print('The biggest distance from the average height among these two people is', biggest_distance_m, 'meters.')