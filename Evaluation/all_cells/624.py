# Shuffle data
images_seq, labels_seq = correspondingShuffle([images_seq, labels_seq])

    
# Split data on train and test dataset
div = int(train_set * len(images_seq))

trainImages = images_seq[0:div]
testImages = images_seq[div:]

trainLabels = labels_seq[0:div]
testLabels = labels_seq[div:]

print("Training images:", div)
print("Testing images:", len(images_seq) - div)