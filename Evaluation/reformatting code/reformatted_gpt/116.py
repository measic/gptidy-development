fig, ax = plt.subplots(figsize=(8, 6))

plot_w = np.arange(K) + 1

ax.bar(plot_w - 0.5, trace['w'].mean(axis=0), width=1., lw=0)

ax.set_xlim(0.5, K)
ax.set_xlabel('Component')

ax.set_ylabel('Posterior expected mixture weight')