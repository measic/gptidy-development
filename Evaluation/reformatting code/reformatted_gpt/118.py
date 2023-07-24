# TODO: Select three indices of your choice you wish to sample from the dataset
indices = [66, 120, 420]

# Create a DataFrame of the chosen samples
samples = pd.DataFrame(data.loc[indices], columns=data.keys()).reset_index(drop=True)
print("Chosen samples of wholesale customers dataset:")
display(samples)