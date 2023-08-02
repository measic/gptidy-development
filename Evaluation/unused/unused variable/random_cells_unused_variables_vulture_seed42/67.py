# probamos con n_components para reduccion pero no afecto
shrinkage = np.linspace(0.1,1.0).tolist()
shrinkage.append('auto')

parametros_LDA_lsqr_eigen = {
    "solver": ["lsqr"],
    "priors": priors,
    "shrinkage": shrinkage,
    "n_components": range(1, 20)
}

(tiempo_LDA_lsqr_eigen, grid_lda) = correr_y_mostrar(
    LDA(),
    parametros_LDA_lsqr_eigen,
    5,
    10
)