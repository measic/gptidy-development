# Generate hypothesis data
def gen_hyp_data(model, N, text_len=500):
    texts, hiddens, hyps = [], [], []
    for i in range(N):
        text, hidden = generate(model, '\n\n', text_len, 0.8, True)
        hidden = hidden.reshape(hidden.shape[0], -1)
        hyp = hypothesis_inlinecounter(text)
        hiddens.append(hidden)
        hyps.append(hyp)
        texts.append(text)
    return ''.join(texts), np.concatenate(hyps), np.concatenate(hiddens)

# Generate train and test data
train_texts, train_hyps, train_hiddens = gen_hyp_data(model_gru, 500)
test_texts, test_hyps, test_hiddens = gen_hyp_data(model_gru, 2)