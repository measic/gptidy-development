if 'p' in globals().keys():
    # Hyper-parameters passed by the experiment runner.
    for key, value in p.items():
        globals()[key] = value
else:
    m = 64  # 64, 128, 512
    ls = 1
    ld = 10
    le = None
    lg = 1
    rtol = 1e-5  # 1e-3, 1e-5, 1e-7
    N_inner = 500
    N_outer = 50
    Ngenres, Nclips, Nframes = 10, 100, 644
    noise_std = 0
    folder = 'data'
    filename_audio = 'audio.hdf5'
    filename_graph = 'graph.hdf5'
    filename_features = 'features.hdf5'