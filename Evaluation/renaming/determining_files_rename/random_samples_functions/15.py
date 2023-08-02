def highlight_column_matches(data, column='', color='yellow'):
    """
    highlight the maximum in a Series or DataFrame
    """
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:
        is_mixed = data == data[column]
        return [attr if v else '' for v in is_mixed]
    else:
        is_mixed = data == data[column]
        return pd.DataFrame(np.where(is_mixed, attr, ''), index=data.index, columns=data.columns)

def function_def(csv_filename, columns=['total_reward'], **kwargs):
    """Plot specified columns from CSV file."""
    df_stats = pd.read_csv(csv_filename)
    df_stats[columns].plot(**kwargs)

def save_rnn_layers(hidden_layers, output_layers):
    for i, layer in hidden_layers.items():
        np.save(os.path.join(vsig.out_dir, 'valid_hidden_layer_' + i + '_output'), hidden_layers[i]['output'])
        np.save(os.path.join(vsig.out_dir, 'valid_hidden_layer_' + i + '_state'), hidden_layers[i]['state'])
    np.save(os.path.join(vsig.out_dir, 'valid_output_layer'), output_layers)

def save_mlp_layers(hidden_layers, output_layers):
    for i, layer in hidden_layers.items():
        np.save(os.path.join(vsig.out_dir, 'valid_hidden_layer_' + i + '_output'), layer)
    np.save(os.path.join(vsig.out_dir, 'valid_output_layer'), output_layers)

def glance_at_tensor(tensor):
    if len(tensor.shape) == 3:
        print(tensor[:10, 0, 0])
        print(tensor[0, :10, 0])
        print(tensor[0, 0, :10])
        print('')
        print(tensor[-10:, -1, -1])
        print(tensor[-1, -10:, -1])
        print(tensor[-1, -1, -10:])
    elif len(tensor.shape) == 4:
        print(tensor[:10, 0, 0, 0])
        print(tensor[0, :10, 0, 0])
        print(tensor[0, 0, :10, 0])
        print(tensor[0, 0, 0, :10])
        print('')
        print(tensor[-10:, -1, -1, -1])
        print(tensor[-1, -10:, -1, -1])
        print(tensor[-1, -1, -10:, -1])
        print(tensor[-1, -1, -1, -10:])
classifier_activation = {'binary': 'sigmoid', 'categorical': 'softmax'}