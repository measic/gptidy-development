#Using the embedding layer of the best performing network of previous exercice. (E["LSTM"])

lstm_embedding = LSTM.layers[1].get_weights()[0]
from keras.initializers import Constant

#Earlystopping criteria
callback = EarlyStopping(monitor='val_acc', min_delta=0.001, patience=2)