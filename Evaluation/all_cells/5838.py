# Load the Iris flower dataset:
iris = datasets.load_iris()
X_iris = iris.data
y = iris.target

X_iris.shape
np.unique(y, axis=0)

plot_data(X_iris, title='Scikit learn iris dataset')