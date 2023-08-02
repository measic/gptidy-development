def full_test(model, hypothesis, name, plot=False, train_len=95, test_len=10,
              ex_name='test'):
    y_true, y_pred = validate_hypothesis(model, LogisticRegression(), hypothesis,
                                         train_len=train_len, test_len=train_len,
                                         save_hyp='plots/hyp_{}.png'.format(ex_name),
                                         save_diag='plots/diag_{}.png'.format(ex_name),
                                         save_resp='plots/resp_{}.png'.format(ex_name))
    metric_pearsonr = lambda a, b: stats.pearsonr(a, b)[0]
    
    print("Hypothesis: {} (normal)".format(name))
    print('acc:      ', metrics.accuracy_score(y_true, y_pred))
    print('prec:     ', metrics.precision_score(y_true, y_pred))
    print('recall:   ', metrics.recall_score(y_true, y_pred))
    print('f1-score: ', metrics.f1_score(y_true, y_pred))
    print('pearsonr: ', metric_pearsonr(y_true, y_pred))
    y_true, y_pred = validate_hypothesis(model, LogisticRegression(class_weight='balanced'),
                                         hypothesis, train_len=train_len, test_len=test_len,
                                         save_hyp='plots/hyp_{}_balanced.png'.format(ex_name),
                                         save_diag='plots/diag_{}_balanced.png'.format(ex_name),
                                         save_resp='plots/resp_{}_balanced.png'.format(ex_name))
    print("Hypothesis: {} (balanced)".format(name))
    print('acc:      ', metrics.accuracy_score(y_true, y_pred))
    print('prec:     ', metrics.precision_score(y_true, y_pred))
    print('recall:   ', metrics.recall_score(y_true, y_pred))
    print('f1-score: ', metrics.f1_score(y_true, y_pred))
    print('pearsonr: ', metric_pearsonr(y_true, y_pred))