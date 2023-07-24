parametersLDA_svd = {
    'solver'            :['svd'],
    'priors'            :priors,
    'n_components'      :randint(1, 300),
}

(tiempo_random_LDA_svd, random_lda_svd) = correr_randomized_y_mostrar(
    LDA(),
    parametersLDA_svd,
    5,
    5,
    30
)

verTiempo(tiempo_LDA_svd, tiempo_random_LDA_svd)