with open("RNNmodel_128_64_log.pkl", "rb") as file:
    logs["RNN"] = pickle.load(file)

with open("LSTMmodel_128_64_log.pkl", "rb") as file:
     logs["LSTM"] = pickle.load(file)

with open("GRUmodel_128_64_log.pkl", "rb") as file:
    logs["GRU"] = pickle.load(file)