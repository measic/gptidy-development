print('\n============== LSTM MODEL ==============\n')
text, hiddens = generate(model_lstm, '\n\n', 500, 0.8, True)
print(text)

print('\n============== GRU MODEL ===============\n')
text, hiddens = generate(model_gru, '\n\n', 500, 0.8, True)
print(text)
