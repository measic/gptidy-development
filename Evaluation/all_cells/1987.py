# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_25K, 'model_25K.pkl')