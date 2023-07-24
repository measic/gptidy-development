print(env.action_space)  # 0 or 1

obs = env.reset()
print(obs)  # position, velocity, angle, angular_velocity
print(env._max_episode_steps)

observation_space_dimension = env.observation_space.shape[0]
print(observation_space_dimension)