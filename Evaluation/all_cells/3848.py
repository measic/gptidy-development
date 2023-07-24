from sklearn.linear_model import LinearRegression
import numpy as np

lregression_model_NNPASTA = LinearRegression()
lregression_model_NNPASTA.fit(np.array(data_1999_2009_sbi[['NNNA-RATIO']]).reshape(-1, 1),
                              np.array(data_1999_2009_sbi[['NNPASTA']]).reshape(-1, 1))