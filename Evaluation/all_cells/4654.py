### Define our Scratch Model 
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential

from keras import backend as K

from keras.callbacks import ModelCheckpoint

NUM_CLASSES = 133  ## Total number of Dog Breeds to classify

K.clear_session()
scratch_model = Sequential()

### TODO: Define your architecture.

INPUT_SHAPE = (224, 224, 3)   # H x W x C for ResNet

scratch_model.add(Conv2D(filters=16, kernel_size=2, padding='valid', activation='relu', 
                        input_shape=INPUT_SHAPE))
scratch_model.add(MaxPooling2D(pool_size=2))
scratch_model.add(Conv2D(filters=32, kernel_size=2, padding='valid', activation='relu'))
scratch_model.add(MaxPooling2D(pool_size=2))
scratch_model.add(Conv2D(filters=64, kernel_size=2, padding='valid', activation='relu'))
scratch_model.add(MaxPooling2D(pool_size=2))

#scratch_model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
#scratch_model.add(MaxPooling2D(pool_size=2))

scratch_model.add(Dropout(0.5))
scratch_model.add(Flatten())
scratch_model.add(Dense(256, activation='relu'))
scratch_model.add(Dropout(0.4))
scratch_model.add(Dense(NUM_CLASSES, activation='softmax'))


scratch_model.summary()