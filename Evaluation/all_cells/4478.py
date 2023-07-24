data_path = "/users/danielcorcoran/desktop/\
github_repos/python_nb_visualization/\
seaborn_official_datasets/iris.csv"

data = pandas.read_csv(data_path)

print("Dataframe has {} features and {} records".format(data.shape[1], data.shape[0]))