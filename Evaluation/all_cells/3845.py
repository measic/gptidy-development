print(round(lregression_model_NIMTA.score(np.array(data_1999_2009_sbi[['WBTE-RATIO']]).reshape(-1, 1),
                                          np.array(data_1999_2009_sbi[['NIMTA-RATIO']]).reshape(-1, 1)), 3))
print(lregression_model_NIMTA.coef_)
print(lregression_model_NIMTA.intercept_)
print(lregression_model_NIMTA.predict(2.33))