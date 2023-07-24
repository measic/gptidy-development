scores = []
nb_episodes = 100

for i in range(0, nb_episodes):
    episode_score = run_episode_neural_network()
    scores.append(episode_score)