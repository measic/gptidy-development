from keras import optimizers
sgd = optimizers.SGD(lr=1e-3, decay=1e-6, momentum=0.9, nesterov=True)
rmsprop = optimizers.RMSprop(lr=1e-4)

#my_VGG16.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
#my_VGG16.compile(optimizer=sgd, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
VGG16Seq.compile(optimizer=rmsprop, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
