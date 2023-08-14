# Using keras to predict outcome
from keras.layers import Dropout
model = Sequential([
    Dense(32, input_shape=(15,)),
    Dropout(0.1),   # Added a dropout layer of 10% to regulate neural network
    Activation('sigmoid'),
    Dense(5),
    Activation('softmax'),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.fit(np.array(X_train), y_train_hot, epochs=10, batch_size=32)