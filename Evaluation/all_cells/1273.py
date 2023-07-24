from sklearn.metrics import mean_squared_error
from math import sqrt

rms_test = sqrt(mean_squared_error(y_test, y_test_predict))
rms_test