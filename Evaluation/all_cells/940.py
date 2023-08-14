from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(-1,1)) # Again storing it as a variable
scaler

# A note about the MinMaxScaler: it transforms features by scaling each feature 
# to a given range. The estimator scales and tanslates each feature individually such that it is 
# in the given range of the traninig set