import pandas as pd

# read in refactoring observations
refactoring_observations = pd.read_csv("4Refactoring_Observations.csv")
all_commits_in_sample = pd.read_csv("6All_Commits_in_Sample.csv")

# join the data sets based on commit_hash and keep only those in refactoring_observations
merged_data = pd.merge(refactoring_observations, all_commits_in_sample, left_on='commit_hash', right_on='commit', how='left')

# remove duplicates
merged_data = merged_data.drop_duplicates()

# filter the merged data frame to only keep those rows where refactor_code matches what I want to keep
keeps = ["efun", "ek", "ev", "t1c", "t2c", "t3c", "rs"]
merged_data = merged_data.loc[merged_data['refactor_code'].isin(keeps)]

# export merged data
# Function to create the string URL
def create_url_before(repo, commit_hash, notebook):
    return f"https://raw.githubusercontent.com/{repo}/{commit_hash}~1/{notebook}"

def create_url_after(repo, commit_hash, notebook):
    return f"https://raw.githubusercontent.com/{repo}/{commit_hash}/{notebook}"

# Create a new column with the URL strings
merged_data['url_before'] = merged_data.apply(lambda x: create_url_before(x['repo'], x['commit_hash'], x['notebook']), axis=1)

# Create a new column with the URL strings
merged_data['url_after'] = merged_data.apply(lambda x: create_url_after(x['repo'], x['commit_hash'], x['notebook']), axis=1)

# keep columns
merged_data = merged_data[['commit_hash', 'refactor_code', 'repo', 'notebook', 'url_before', 'url_after']]

merged_data.to_csv("dataset1.csv", index=False)
