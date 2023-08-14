# Create Dataset
from sklearn.model_selection import train_test_split

X, y = make_moons(n_samples=500, noise=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

X_train_1, X_train_2, y_train_1, y_train_2 = train_test_split(X_train, y_train, random_state=42)
