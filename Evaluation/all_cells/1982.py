# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_Half, 'model_Half.pkl')