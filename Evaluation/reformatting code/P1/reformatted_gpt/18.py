# Just read and run this cell.

aditya_height_m = 1.21
botan_height_m = 1.85
average_adult_human_height_m = 1.688

# The biggest distance from the average human height, among the two heights:
biggest_distance_m = max(
    abs(aditya_height_m - average_adult_human_height_m),
    abs(botan_height_m - average_adult_human_height_m)
)

# Print out our results in a nice readable format:
print("The biggest distance from the average height among these two people is",
      biggest_distance_m, "meters.")