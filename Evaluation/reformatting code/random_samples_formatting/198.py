n_pred = 200
X_new = np.linspace(0, 2.0, n_pred)[:,None]

with model:
    f_pred = gp.conditional("f_pred", X_new)

with model:
    pred_samples = pm.sample_ppc(trace, vars=[f_pred], samples=1000)