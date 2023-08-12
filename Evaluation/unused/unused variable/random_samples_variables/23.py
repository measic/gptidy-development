y_true, y_pred = validate_hypothesis(model, LinearRegression(), hypothesis_inlinecounter,
                                     train_len=95, test_len=5,
                                     save_hyp='plots/hyp_inlinecounter_shake.png',
                                     save_diag='plots/diag_inlinecounter_shake.png',
                                     save_resp='plots/resp_inlinecounter_shake.png')