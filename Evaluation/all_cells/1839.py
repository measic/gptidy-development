X_train_dog = X_train_feature
X_train_dog = X_train_feature.drop('AnimalType_Dog', 1)
X_dev_dog = X_dev_feature
X_dev_dog = X_dev_feature.drop('AnimalType_Dog', 1)

model3 = Sequential([
    Dense(32, input_shape=(12,)),
    Dropout(0.1),  
    Activation('sigmoid'),
    Dense(5),
    Activation('softmax'),
])

model3.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model3.fit(np.array(X_train_dog), y_train_hot, epochs=10, batch_size=32)