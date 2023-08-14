# Save the model as a pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_5K, 'model_5K.pkl')