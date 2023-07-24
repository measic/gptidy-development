# plot the results
fig = plt.figure(figsize=(12,5)); ax = fig.gca()

# plot the samples from the gp posterior with samples and shading
plot_gp_dist(ax, invlogit(trace["f"]), x);

# plot the data (with some jitter) and the true latent function
plt.plot(x, invlogit(f_true), "dodgerblue", lw=3, label="True f");
plt.plot(x, y + np.random.randn(y.shape[0])*0.01, 'ok', ms=3, alpha=0.5, label="Observed data");

# axis labels and title
plt.xlabel("X"); plt.ylabel("True f(x)"); 
plt.title("Posterior distribution over $f(x)$ at the observed values"); plt.legend();