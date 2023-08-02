def function_def(model, N, text_len=500):
    texts, hiddens, hyps = ([], [], [])
    for i in range(N):
        text, hidden = generate(model, '\n\n', text_len, 0.8, True)
        hidden = hidden.reshape(hidden.shape[0], -1)
        hyp = hypothesis_inlinecounter(text)
        hiddens.append(hidden)
        hyps.append(hyp)
        texts.append(text)
    return (''.join(texts), np.concatenate(hyps), np.concatenate(hiddens))
train_texts, train_hyps, train_hiddens = function_def(model_gru, 500)
test_texts, test_hyps, test_hiddens = function_def(model_gru, 2)