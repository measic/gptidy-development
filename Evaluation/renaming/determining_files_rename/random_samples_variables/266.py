cov = X.T @ X / (X.shape[0] - 1)
val, vec = np.linalg.eigh(cov)
idx = np.argsort(val)[::-1]
val = val[idx]
vec = vec[:, idx]
project_X = X @ vec
variable_def = vec.T @ vec
inversed_vec = np.linalg.inv(vec)
inversed_vec = inversed_vec - inversed_vec.mean(1)
revert_X = project_X @ inversed_vec
revertedV = variable_def @ inversed_vec.T

def plot():
    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', alpha=0.5)
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', alpha=0.5)
    pca11 = plt.arrow(0, 0, *vec[:, 0] * val[0], head_width=0.05, head_length=0.05, color='Green', label='First PC')
    pca12 = plt.arrow(0, 0, *vec[:, 1] * val[1], head_width=0.05, head_length=0.05, color='magenta', label='Second PC')
    plt.grid(True)
    plt.subplot(132)
    plt.scatter(project_X[y == 0, 0], project_X[y == 0, 1], color='red', alpha=0.5)
    plt.scatter(project_X[y == 1, 0], project_X[y == 1, 1], color='blue', alpha=0.5)
    pca21 = plt.arrow(0, 0, *variable_def[:, 0] * val_reduced[0], head_width=0.05, head_length=0.05, color='Green', label='First PC')
    pca22 = plt.arrow(0, 0, *variable_def[:, 1] * val_reduced[1], head_width=0.05, head_length=0.05, color='magenta', label='Second PC')
    plt.grid(True)
    plt.subplot(133)
    plt.scatter(revert_X[y == 0, 0], revert_X[y == 0, 1], color='red', alpha=0.5)
    plt.scatter(revert_X[y == 1, 0], revert_X[y == 1, 1], color='blue', alpha=0.5)
    pca21 = plt.arrow(0, 0, *revertedV[:, 0] * val[0], head_width=0.05, head_length=0.05, color='Green', label='First PC')
    pca22 = plt.arrow(0, 0, *revertedV[:, 1] * val[1], head_width=0.05, head_length=0.05, color='magenta', label='Second PC')
    plt.grid(True)
    plt.show()
plot()