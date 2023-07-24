from distutils.version import LooseVersion as Version
from sklearn import __version__ as sklearn_version


if Version(sklearn_version) < '0.18':
    clf = SGDClassifier(loss='log', random_state=1, n_iter=1)
else:
    clf = SGDClassifier(loss='log', random_state=1, max_iter=1)


doc_stream = stream_docs(path='movie_data.csv')