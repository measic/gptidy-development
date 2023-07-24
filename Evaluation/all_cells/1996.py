# Save the model as pickle file

import pickle
from sklearn.externals import joblib

joblib.dump(model_40K, 'model_40K.pkl')