## @Readers: PLEASE IGNORE THIS CELL
##
## This cell is meant to create a smaller dataset if
## the notebook is run on the Travis Continuous Integration
## platform to test the code on a smaller dataset
## to prevent timeout errors and just serves a debugging tool
## for this notebook

if 'TRAVIS' in os.environ:
    df.loc[:500].to_csv('movie_data.csv')
    df = pd.read_csv('movie_data.csv', nrows=500)
    print('SMALL DATA SUBSET CREATED FOR TESTING')