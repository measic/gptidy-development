def function_def(env, estimator_policy, estimator_value, num_episodes, discount_factor=1.0):
    """
    Actor Critic Algorithm. Optimizes the policy 
    function approximator using policy gradient.
    
    Args:
        env: OpenAI environment.
        estimator_policy: Policy Function to be optimized 
        estimator_value: Value function approximator, used as a critic
        num_episodes: Number of episodes to run for
        discount_factor: Time-discount factor
    
    Returns:
        An EpisodeStats object with two numpy arrays for episode_lengths and episode_rewards.
    """
    stats = plotting.EpisodeStats(episode_lengths=np.zeros(num_episodes), episode_rewards=np.zeros(num_episodes))
    Transition = collections.namedtuple('Transition', ['state', 'action', 'reward', 'next_state', 'done'])
    for i_episode in range(num_episodes):
        state = env.reset()
        episode = []
        for t in itertools.count():
            action = estimator_policy.predict(state)
            next_state, reward, done, _ = env.step(action)
            episode.append(Transition(state=state, action=action, reward=reward, next_state=next_state, done=done))
            stats.episode_rewards[i_episode] += reward
            stats.episode_lengths[i_episode] = t
            value_next = estimator_value.predict(next_state)
            td_target = reward + discount_factor * value_next
            td_error = td_target - estimator_value.predict(state)
            estimator_value.update(state, td_target)
            estimator_policy.update(state, td_error, action)
            print('\rStep {} @ Episode {}/{} ({})'.format(t, i_episode + 1, num_episodes, stats.episode_rewards[i_episode - 1]), end='')
            if done:
                break
            state = next_state
    return stats