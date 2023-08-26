def validate_hypothesis(model, diag_classifier, hypothesis, train_len=50, test_len=1, text_len=500, temperature=0.8, save_hyp=None, save_diag=None, save_resp=None):

    def gen_hyp_data(model, N, text_len=500):
        texts, hiddens, hyps = ([], [], [])
        for i in range(N):
            text, variable_def = generate(model, '\n\n', text_len, temperature, True)
            variable_def = variable_def.reshape(variable_def.shape[0], -1)
            hyp = hypothesis(text)
            hiddens.append(variable_def)
            hyps.append(hyp)
            texts.append(text)
        return (''.join(texts), np.concatenate(hyps), np.concatenate(hiddens))
    _, train_hyps, train_hiddens = gen_hyp_data(model, train_len)
    test_texts, test_hyps, test_hiddens = gen_hyp_data(model, test_len)
    print(pearsonr(train_hiddens, train_hyps))
    print(pearsonr(test_hiddens, test_hyps))
    diag_classifier.fit(train_hiddens, train_hyps)
    pred_hyps = diag_classifier.predict(test_hiddens)
    resp_neuron = np.argmax(np.abs(diag_classifier.coef_))
    print(resp_neuron)
    if save_hyp:
        plot_colored_text(test_texts[:text_len], test_hyps[:text_len], title='Formed Hypothesis', save_file=save_hyp)
    if save_diag:
        plot_colored_text(test_texts[:text_len], pred_hyps[:text_len], title='Diagnostic Classifier Prediction', save_file=save_diag)
    if save_resp:
        plot_colored_text(test_texts[:text_len], test_hiddens[:text_len, resp_neuron], title='Most Responsible Neuron {}'.format(resp_neuron), save_file=save_resp)
    del train_hyps
    del train_hiddens
    del test_texts
    del test_hiddens
    gc.collect()
    return (test_hyps, pred_hyps)