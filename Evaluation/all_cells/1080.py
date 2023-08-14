nb_labels = y_train.shape[0]
print("Number of labels for training process : "+str(nb_labels))
VGG16Seq.add(Flatten())  # Conversion des matrices 3D en vecteur 1D