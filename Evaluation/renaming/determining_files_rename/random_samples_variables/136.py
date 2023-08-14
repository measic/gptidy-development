from keras import optimizers
sgd = optimizers.SGD(lr=0.001, decay=1e-06, momentum=0.9, nesterov=True)
variable_def = optimizers.RMSprop(lr=0.0001)
VGG16Seq.compile(optimizer=variable_def, loss='sparse_categorical_crossentropy', metrics=['accuracy'])