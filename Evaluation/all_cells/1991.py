# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_35K, 'model_35K.pkl')