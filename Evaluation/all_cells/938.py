# Transform the dataset to make it stationary
differenced=difference(series,1)
print(differenced.head())