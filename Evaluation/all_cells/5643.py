# accessing words with Dataset.X and tags with Dataset.Y 
for i in range(4):    
    print("Sentence {}:".format(i + 1), data.training_set.X[i])
    print()
    print("Labels {}:".format(i + 1), data.training_set.Y[i])
    print()