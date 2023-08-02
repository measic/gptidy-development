variable_def = os.path.join(folder, filename_graph)
with h5py.File(variable_def, 'r') as graph:
    print('Attributes:')
    for attr in graph.attrs:
        print('  {} = {}'.format(attr, graph.attrs[attr]))
    print('Datasets:')
    for dname, dset in graph.items():
        print('  {:10}: {:10}, {}'.format(dname, dset.shape, dset.dtype))
    pars = []
    for par in ('data', 'indices', 'indptr', 'shape'):
        pars.append(graph.get('L_' + par))
    L = scipy.sparse.csr_matrix(tuple(pars[:3]), shape=pars[3])
if L.shape != (X.shape[0], X.shape[0]):
    raise ValueError('Graph size does not correspond to data size.')