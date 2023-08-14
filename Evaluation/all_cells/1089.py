print(arr_X_train.shape)
history = VGG16Seq.fit(arr_X_train, arr_y_train, epochs=50, batch_size=90,verbose=1,validation_data=(arr_X_test, arr_y_test))