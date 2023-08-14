nb_episodes = 1000
positions = []
velocities = []
angles = []
angular_velocities = []

for episode in range(0, nb_episodes):
    obs = env.reset()
    done = False
    final_score = 0

    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        position, velocity, angle, angular_velocity = obs
        positions.append(position)
        velocities.append(velocity)
        angles.append(angle)
        angular_velocities.append(angular_velocity)        