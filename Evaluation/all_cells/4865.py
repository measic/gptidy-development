#reshape dataset and target for RNN
#context
X_ = np.array(padded_X)
#answer
padded_T = np.array(padded_T)

#one hot encoding of answer --> target T
T_ = keras.utils.to_categorical(padded_T)