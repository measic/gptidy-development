val_arrays = np.load(os.path.join(vsig.out_dir, 'valid_output_layer.npy'))
print(val_arrays.shape)
glance_at_tensor(val_arrays)