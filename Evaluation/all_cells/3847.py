print(round(lregression_model_NNPASTA.score(np.array(data_1999_2009_sbi[['NNNA-RATIO']]).reshape(-1, 1),
                                            np.array(data_1999_2009_sbi[['NNPASTA']]).reshape(-1, 1)), 3))
print(lregression_model_NNPASTA.coef_)
print(lregression_model_NNPASTA.intercept_)
print(lregression_model_NNPASTA.predict(4.12))