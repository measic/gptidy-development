def encode_io_pairs(text, window_size, step_size):
    variable_def = sorted(list(set(text)))
    num_chars = len(variable_def)
    inputs, outputs = window_transform_text(text, window_size, step_size)
    X = np.zeros((len(inputs), window_size, num_chars), dtype=np.bool)
    y = np.zeros((len(inputs), num_chars), dtype=np.bool)
    for i, sentence in enumerate(inputs):
        for t, char in enumerate(sentence):
            X[i, t, chars_to_indices[char]] = 1
        y[i, chars_to_indices[outputs[i]]] = 1
    return (X, y)