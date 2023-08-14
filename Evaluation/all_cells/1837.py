X_train_feature = X_train
X_train_feature = X_train_feature.drop('Intact_Unknown', 1)
X_train_feature = X_train_feature.drop('Female_Unknown', 1)
X_dev_feature = X_dev
X_dev_feature = X_dev_feature.drop('Intact_Unknown', 1)
X_dev_feature = X_dev_feature.drop('Female_Unknown', 1)

model2 = Sequential([
    Dense(32, input_shape=(13,)),
    Dropout(0.1),   
    Activation('sigmoid'),
    Dense(5),
    Activation('softmax'),
])

model2.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model2.fit(np.array(X_train_feature), y_train_hot, epochs=10, batch_size=32)