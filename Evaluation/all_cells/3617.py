scores = []
for rep in range(number_of_replicates):
    env.reset()
    done = False
    episode_score = 0.0
    while not done:
        action = np.random.binomial(1, 0.3)
        _, r, done = env.step(action)
        episode_score += r
    scores.append(episode_score)
print('mean score: {} se: {}'.format(np.mean(scores), np.std(scores) / np.sqrt(number_of_replicates)))