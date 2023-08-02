t_min_max = (vsig.timestamps[0], vsig.timestamps[-1])
layer = '2'
o_or_s = 'output'
val_arrays = np.load(os.path.join(vsig.out_dir, '_'.join(['valid_hidden_layer', layer, o_or_s])) + '.npy')
n_generations, _, n_neurons = val_arrays.shape
variable_def = 2
nrows = n_neurons // variable_def
fig, axes = plt.subplots(nrows=nrows, ncols=variable_def, figsize=(16, 20))
for g in range(n_generations):
    for i in range(n_neurons):
        ax = axes[i // variable_def, i % variable_def]
        ax.cla()
        y_pred_colors = val_arrays[g, :, i]
        ax.plot(vsig.timestamps, vsig.mixed_signal, color='grey', alpha=0.3)
        ax.scatter(vsig.timestamps, x_val[0, :, 0], vsig.timestamps[vsig.window_size - 1:], marker='o', c=y_pred_colors, cmap=plt.get_cmap('coolwarm'), vmin=-1, vmax=1)
        ax.set_title('neuron = {}'.format(i + 1))
        ax.set_xlim(t_min_max)
        ax.grid(True)
    plt.tight_layout()
    plt.suptitle('hidden layer = {}, ({}), generation = {}'.format(layer, o_or_s, g + 1))
    plt.savefig(os.path.join(vsig.out_dir, '_'.join(['valid_hidden_layer', layer, o_or_s, 'gen', str(g + 1)]) + '.png'))
plt.show()