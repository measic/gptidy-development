from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MultiLabelBinarizer

v = DictVectorizer()
X = v.fit_transform(X_train)
Xt = v.transform(X_test)