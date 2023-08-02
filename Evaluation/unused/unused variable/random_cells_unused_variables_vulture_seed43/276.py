parametersNaiveBayes = {
    'priors':priors
}

(tiempo_random_bayes, random_bayes) = correr_randomized_y_mostrar(
    GaussianNB(), 
    parametersNaiveBayes, 
    5, 
    5
)

verTiempo(tiempo_bayes, tiempo_random_bayes)