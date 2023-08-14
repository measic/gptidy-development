### Preprocess the data here. It is required to normalize the data. Other preprocessing steps could include 
### converting to grayscale, etc.
### Feel free to use as many code cells as needed.
X_train =  normalize_and_grayscale(X_train)
X_valid =  normalize_and_grayscale(X_valid)
X_test =  normalize_and_grayscale(X_test)