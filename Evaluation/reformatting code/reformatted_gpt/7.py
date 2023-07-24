parametersKNN = {
    'n_neighbors': list(range(1, 32)),
    'weights': ['uniform', 'distance']
}

(tiempo_KNN, grid_knn) = correr_y_mostrar(
    KNeighborsClassifier(),
    parametersKNN,
    5,
    10
)