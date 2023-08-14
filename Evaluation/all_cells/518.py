for model_name, model in [('linux_lstm', model_lstm), ('linux_gru', model_gru)]:
    print("MODEL: ", model_name)
    y_true, y_pred = validate_hypothesis(model, LinearRegression(), hypothesis_inlinecounter,
                                         train_len=95, test_len=1,
                                         save_hyp='plots/{}_hyp_inlinecounter.png'.format(model_name),
                                         save_diag='plots/{}_diag_inlinecounter.png'.format(model_name),
                                         save_resp='plots/{}_resp_inlinecounter.png'.format(model_name))