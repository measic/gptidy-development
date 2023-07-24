filename = os.path.join(folder, filename_audio)
with h5py.File(filename, 'r') as audio:

    # Display HDF5 attributes.
    print('Attributes:')
    for attr in audio.attrs:
        print('  {} = {}'.format(attr, audio.attrs[attr]))
    sr = audio.attrs['sr']
    labels = audio.attrs['labels']

    # Show datasets, their dimensionality and data type.
    print('Datasets:')
    for dname, dset in audio.items():
        print('  {:2}: {:24}, {}'.format(dname, dset.shape, dset.dtype))

    # Choose dataset: Xa, Xs.
    X = audio.get('Xs')

    # Full dataset.
    n = X.shape[-1]
    datinfo(X, 'Full dataset')
    print(type(X))

    # Load data into memory as a standard NumPy array.
    X = X[:Ngenres,:Nclips,:Nframes,...]
    datinfo(X, 'Reduced dataset')
    print(type(X))

    # Resize in place without memory loading via hyperslab.
    # Require chunked datasets.
    #X.resize((Ngenres, Nclips, Nframes, 2, n))

# Squeeze dataset to a 2D array. The auto-encoder does not
# care about the underlying structure of the dataset.
X.resize(Ngenres * Nclips * Nframes * 2, n)
print('Data: {}, {}'.format(X.shape, X.dtype))

# Independently rescale each feature.
# To be put in an sklearn Pipeline to avoid transductive learning.
X -= np.min(X, axis=0)
X /= np.max(X, axis=0)

# Independently normalize each sample.
#X /= np.linalg.norm(X, axis=1)[:,np.newaxis]

# Add Gaussian noise.
if noise_std is not 0:
    X += np.random.normal(scale=noise_std, size=X.shape)