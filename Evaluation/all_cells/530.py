for i in range(200):
    plot_colored_text(train_texts[:500], train_hiddens[:500, i],
                      title='Most Responsible Neuron {}'.format(i),
                      save_file='plots/temp_{}.png'.format(i))
