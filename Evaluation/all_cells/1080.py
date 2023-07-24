# Ajout de la deuxième couche de convolution, suivie  d'une couche ReLU
VGG16Seq.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
VGG16Seq.add(Conv2D(64, (3, 3), activation='relu'))
VGG16Seq.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))