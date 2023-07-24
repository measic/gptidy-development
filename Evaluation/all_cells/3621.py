scores = []
for rep in range(number_of_replicates):
    env.reset()
    done = False
    episode_score = 0.0
    while not done:
        action, pairwise_kernel_, kernel_sums = \
            model_smoothed_fitted_q(env, gamma, RandomForestRegressor, number_of_value_iterations, transition_model_fitter,
                                    pairwise_kernels_=None, kernel_sums=None)
        _, r, done = env.step(action)
        episode_score += r
    scores.append(episode_score)
print('mean score: {} se: {}'.format(np.mean(scores), np.std(scores) / np.sqrt(number_of_replicates)))