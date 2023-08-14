import numpy as np
from sklearn.linear_model import LinearRegression
data_1999_2009_sbi = data_1999_2009_sbi.T

lregression_model_ROA = LinearRegression()
lregression_model_ROA.fit(np.array(data_1999_2009_sbi[['BTA-RATIO']]).reshape(-1, 1),
                          np.array(data_1999_2009_sbi[['ROA']]).reshape(-1, 1))