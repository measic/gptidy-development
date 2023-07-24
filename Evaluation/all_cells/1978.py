# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_15K, 'model_15K.pkl')