# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_10K, 'model_10K.pkl')