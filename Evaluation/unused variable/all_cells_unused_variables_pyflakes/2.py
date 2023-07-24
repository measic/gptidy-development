def run_episode_neural_network(show_renderer=False):    
    with tf.Session() as sess:
        init.run()
        obs = env.reset()
        obs_pretty = obs.reshape(1, nb_neurons_input)
        done = False
        final_score = 0
        while not done:
            if show_renderer:
                env.render()
            proba_move_to_left = output.eval(feed_dict={X: obs_pretty})        
            if random.uniform(0, 1) < proba_move_to_left:
                action = 0  # move to left
            else:
                action = 1       
            obs, reward, done, info = env.step(action) 
            if done:
                break
            final_score += reward
    env.reset()
    env.close()
    return final_score