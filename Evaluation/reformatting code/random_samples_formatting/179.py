import p5_util
filename='./data/arr_keras_X_y_train_test.dump'
(arr_X_train,arr_X_test, arr_y_train, arr_y_test) = p5_util.object_load(filename)
print(arr_X_train.shape,arr_X_test.shape,arr_y_train.shape,arr_y_test.shape)

#### Data normalization

arr_X_train = arr_X_train.astype('float32')
arr_X_test = arr_X_test.astype('float32')

# Scale the data to lie between 0 to 1
arr_X_train /= 255
arr_X_test /= 255