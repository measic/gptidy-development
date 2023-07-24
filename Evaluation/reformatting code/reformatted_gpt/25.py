## @Readers: PLEASE IGNORE THIS CELL
##
## This cell is meant to generate more 
## "logging" output when this notebook is run 
## on the Travis Continuous Integration
## platform to test the code as well as
## speeding up the run using a smaller
## dataset for debugging

if 'TRAVIS' in os.environ:
    gs_lr_tfidf.verbose = 2
    X_train = df.loc[:250, 'review'].values
    y_train = df.loc[:250, 'sentiment'].values
    X_test = df.loc[25000:25250, 'review'].values
    y_test = df.loc[25000:25250, 'sentiment'].values