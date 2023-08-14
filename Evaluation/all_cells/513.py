model_lstm = torch.load('models/linux_3x512_0d3_lstm_200l_40000E.model').cuda()
model_gru = torch.load('models/linux_3x512_0d3_gru_200l_40000E.model').cuda()
print('Perplexity LSTM:', 2**np.mean([test_model(model_lstm, 'data/linux/test.txt') for _ in range(1)]))
print('Perplexity GRU: ', 2**np.mean([test_model(model_gru, 'data/linux/test.txt') for _ in range(1)]))