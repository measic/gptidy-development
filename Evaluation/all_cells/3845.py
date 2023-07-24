print(round(lregression_model_ROA.score(np.array(data_1999_2009_sbi[['BTA-RATIO']]).reshape(-1, 1),
                                        np.array(data_1999_2009_sbi[['ROA']]).reshape(-1, 1)), 3))
print(lregression_model_ROA.coef_)
print(lregression_model_ROA.intercept_)
print(lregression_model_ROA.predict(1.12))