parametersNaiveBayes = {
    'priors':priors
}

(tiempo_bayes, grid_bayes) = correr_y_mostrar(
    GaussianNB(), 
    parametersNaiveBayes, 
    5, 
    5
)