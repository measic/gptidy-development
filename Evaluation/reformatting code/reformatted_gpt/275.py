filename = os.path.join(folder, filename_features)

# Remove existing HDF5 file without warning if non-existent.
try:
    os.remove(filename)
except OSError:
    pass

# Create HDF5 file and datasets.
with h5py.File(filename, 'w') as features:

    # Metadata.
    features.attrs['sr'] = sr
    features.attrs['labels'] = labels

    # Data.
    features.create_dataset('X', data=X.reshape(Ngenres, Nclips, Nframes, 2, n))
    features.create_dataset('Z', data=Z.reshape(Ngenres, Nclips, Nframes, 2, Z.shape[-1]))
    if ld is not None:
        features.create_dataset('D', data=ae.D)
    if le is not None:
        features.create_dataset('E', data=ae.E)

    # Show datasets, their dimensionality and data type.
    print('Datasets:')
    for dname, dset in features.items():
        print('  {:2}: {:22}, {}'.format(dname, dset.shape, dset.dtype))

    # Display HDF5 attributes.
    print('Attributes:')
    for name, value in features.attrs.items():
        print('  {} = {}'.format(name, value))

print('Overall time: {:.0f} seconds'.format(time.time() - toverall))