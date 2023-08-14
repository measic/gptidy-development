parametersLDA = {
    "solver": ["lsqr", "eigen"],
    "priors": priors,
    "shrinkage": uniform(0.1, 0.9),
    "n_components": randint(1, 400)
}

(tiempo_random_LDA_lsqr_eigen, grid_lda) = correr_randomized_y_mostrar(
    LDA(),
    parametersLDA,
    5,
    10,
    10
)

verTiempo(tiempo_LDA_lsqr_eigen, tiempo_random_LDA_lsqr_eigen)