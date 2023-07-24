from scipy.stats import gamma

parametersSVM = {
    'C':gamma(a=1.0, loc=0, scale=0.001)
}

(tiempo_random_SVM, grid_svm) = correr_randomized_y_mostrar(
    LinearSVC(),
    parametersSVM,
    5,
    5,
    30
)

verTiempo(tiempo_SVM, tiempo_random_SVM)