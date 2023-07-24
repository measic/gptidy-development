with model:
    advi = pm.ADVI()
    %time advi.fit(10000, more_replacements={X_shared: X_minibatch},obj_optimizer= pm.adagrad(learning_rate=1e-2))
plt.plot(advi.hist);