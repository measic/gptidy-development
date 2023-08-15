#reshape dataset and target for RNN
list_sentences = [s for c in filtered_sentences for s in c]
X = np.array(list_sentences.copy())

#one hot encoding of X for target T
T = keras.utils.to_categorical(np.asarray(X))