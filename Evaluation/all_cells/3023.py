# y_pred = np.argmax(states['y_hat'], axis=1)
# y_pred_colors = np.hstack([vsig.signal_colors[i] for i in y_pred])
t_min_max = (vsig.timestamps[0], vsig.timestamps[-1])
layer = '1'
val_arrays = np.load(os.path.join(vsig.out_dir, 'valid_hidden_layer_' + layer + '_output.npy'))
n_generations, _, n_neurons = val_arrays.shape
ncols = 1
nrows = n_neurons // ncols
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 3))

for g in range(n_generations):
    for i in range(n_neurons):
        ax = axes#[i // ncols, i % ncols]
        ax.cla()
        y_pred_colors = val_arrays[g, :, i]
        ax.plot(vsig.timestamps, vsig.mixed_signal, color='grey', alpha=0.3)
        ax.scatter(
            vsig.timestamps[vsig.window_size-1:], 
#             vsig.timestamps, 
#             x_val[:, -1, 0], 
#             x_val[0, :, 0], 
            vsig.mixed_signal[vsig.window_size-1:], 
            marker='o', 
            c=y_pred_colors, 
            cmap=plt.get_cmap('coolwarm'), 
            vmin=-1, 
            vmax=1
        )
        ax.set_title('neuron = {}'.format(i + 1))
        ax.set_xlim(t_min_max)
        ax.grid(True)
        
    plt.tight_layout()
    plt.suptitle('hidden layer = {}, ({}), generation = {}'.format(layer, 'output', g + 1))
#     plt.savefig(os.path.join(vsig.out_dir, '_'.join(['valid_hidden_layer', layer, 'gen', str(g + 1)]) + '.png'))

plt.show()