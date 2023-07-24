# Increasing the feature space
i=0
for item in X['bed_type'].unique():
    a=X['bed_type'] == X['bed_type'].unique()[i]
    X[item] = a.map(lambda x: 1 if x == True else 0)
    i=i+1
X.shape