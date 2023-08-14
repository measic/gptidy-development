from scipy.stats import uniform

parametersKNN = {
    'n_neighbors' : randint(1, 360),
    'weights'     : ['uniform', 'distance']
}

(tiempo_random_KNN, random_knn) = correr_randomized_y_mostrar(
    KNeighborsClassifier(), 
    parametersKNN, 
    5, 
    10,
    200
)

verTiempo(tiempo_KNN, tiempo_random_KNN)