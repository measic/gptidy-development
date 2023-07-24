#### Define our Model #####

### TODO: Define your architecture.

K.clear_session()

## Define our extension to the InceptionV3 model
inception_bneck = Sequential()
# input shape is M x 5 x 5 x 2048
inception_bneck.add(GlobalAveragePooling2D(input_shape=train_incp_bn.shape[1:]))
inception_bneck.add(Activation('relu'))
inception_bneck.add(Dense(1024, activation='relu'))
inception_bneck.add(Dropout(0.5))
inception_bneck.add(Dense(512, activation='relu'))
inception_bneck.add(Dropout(0.5))
inception_bneck.add(Dense(NUM_CLASSES, activation='softmax'))

inception_bneck.summary()