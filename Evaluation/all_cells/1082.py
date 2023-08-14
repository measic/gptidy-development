import numpy as np
# Ajout de la dernière couche fully-connected qui permet de classifier
VGG16Seq.add(Dense(nb_labels, activation='softmax'))