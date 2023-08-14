parametros_LDA_svd = {
    'solver'            :['svd'],
    'priors'            :priors,
    'n_components'      :[0, 1, 2, 3, 4, 5, 6],
}

(tiempo_LDA_svd, grid_lda_svd) = correr_y_mostrar(
    LDA(),
    parametros_LDA_svd,
    5,
    5
)