from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten, Dense, Dropout

VGG16Seq = Sequential()  # Création d'un réseau de neurones vide 

# Ajout de la première couche de convolution, suivie d'une couche ReLU
w=X_train.shape[1]
h=X_train.shape[2]
c=X_train.shape[3]
print(w,h,c)
VGG16Seq.add(Conv2D(64, (3, 3), input_shape=(w, h, c), padding='same', activation='relu'))
VGG16Seq.add(Conv2D(64, (3, 3), activation='relu'))
VGG16Seq.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))