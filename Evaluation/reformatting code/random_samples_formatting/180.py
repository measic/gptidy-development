## TO BE REMOVED!
scores = []
for x, t in zip(x_valid, t_valid):
    _, _, logp_valid = logprob(x, w, b)
    pred = np.argmax(logp_valid)
    scores.append(1 if pred == t else 0)
print(mean(scores))