lregression_model_NIMTA = LinearRegression()
lregression_model_NIMTA.fit(np.array(data_1999_2009_sbi[['WBTE-RATIO']]).reshape(-1, 1),
                            np.array(data_1999_2009_sbi[['NIMTA-RATIO']]).reshape(-1, 1))