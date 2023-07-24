logp = []
for x, t in zip(x_valid, t_valid):
    _, _, logp_valid = logprob(x, w, b)
    logp.append(logp_valid[t])

data = list(zip(logp, x_valid, t_valid))
data.sort(key=lambda tup: tup[0])

# hardest 8 digits
xs = np.array([d[1] for d in data[:8]])
ts = np.array([d[2] for d in data[:8]])

plt.suptitle('8 hardest digitis', y = 1.05)
plot_digits(xs, num_cols=4, targets=ts)

# easiest 8 digits
xs = np.array([d[1] for d in data[-8:]])
ts = np.array([d[2] for d in data[-8:]])

plt.suptitle('8 easiest digitis', y = 1.05)
plot_digits(xs, num_cols=4, targets=ts)