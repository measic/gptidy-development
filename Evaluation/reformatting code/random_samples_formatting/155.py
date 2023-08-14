fig = plt.figure(figsize=(12,5)); ax = fig.gca()
ax.plot(x, invlogit(f_true), 'dodgerblue', lw=3, label="True rate");
ax.plot(x, y + np.random.randn(n)*0.01, 'ko', ms=3, label="Observed data");
ax.set_xlabel("X"); ax.set_ylabel("y"); plt.legend();