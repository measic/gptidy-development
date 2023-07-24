parametersSVM = {
    'C':[1e-15, 1e-10, 1e-5, 1e-4, 1e-3, 1e-2, 1.0],
}

(tiempo_SVM, grid_svm) = correr_y_mostrar(
    LinearSVC(), 
    parametersSVM, 
    5,
    5
)