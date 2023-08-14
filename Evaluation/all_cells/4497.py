unique_datatypes = list(merged["data_type"].unique())

print("Unique datatypes in this dataset are: {}".format(unique_datatypes))

if "float64" in unique_datatypes or "int64" in unique_datatypes:
    
    round_values = True
    rounded_places = 4
    
    for column in ["mean", "std", "min", "25%", "50%", "75%", "max"]:
        
        merged[column] = merged[column].astype(float).round(rounded_places)
else:
    round_values = False