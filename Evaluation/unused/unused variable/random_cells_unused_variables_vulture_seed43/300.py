X_train_cat = X_train_feature
X_train_cat = X_train_feature.drop('AnimalType_Cat', 1)
X_dev_cat = X_dev_feature
X_dev_cat = X_dev_feature.drop('AnimalType_Cat', 1)

model4 = Sequential([
    Dense(32, input_shape=(12,)),
    Dropout(0.1),   
    Activation('sigmoid'),
    Dense(5),
    Activation('softmax'),
])

model4.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model4.fit(np.array(X_train_cat), y_train_hot, epochs=10, batch_size=32)