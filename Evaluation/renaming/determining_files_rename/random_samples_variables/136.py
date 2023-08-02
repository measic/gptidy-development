from keras import optimizers
variable_def = optimizers.SGD(lr=0.001, decay=1e-06, momentum=0.9, nesterov=True)
rmsprop = optimizers.RMSprop(lr=0.0001)
VGG16Seq.compile(optimizer=rmsprop, loss='sparse_categorical_crossentropy', metrics=['accuracy'])