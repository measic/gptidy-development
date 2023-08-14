layer = '1'
o_or_s = 'output'
val_arrays = np.load(os.path.join(vsig.out_dir, '_'.join(['valid_hidden_layer', layer, o_or_s])) + '.npy')
print(val_arrays.shape)
glance_at_tensor(val_arrays)