# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_30K, 'model_30K.pkl')