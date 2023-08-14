os.makedirs('tmp/precipitation', exist_ok=True)
os.makedirs('tmp/pet', exist_ok=True)
os.makedirs('ws_mask/amazonas', exist_ok=True)

d0, d1 = '2000-03-01 12:00:00', '2018-12-31'
x_range = ((0.1, 1e4), (-1, 1), (0.1, 1e3), (0.1, 1e2))
draws = 100
warmup = 12 * 30 * 24 * 2 # one year in 30min steps
n_pdf = 10

x_pdf = {}
for down_label in labels_with_vs_tree:
    vs = labels_with_vs[down_label]
    for s in vs:
        print(df_vs.query(f"station == '{s}'").iloc[0])
    # get whole basin's labels
    whole_labels = startswith_label(down_label, all_labels)
    # copy basin's masks locally
    for label in whole_labels:
        if not os.path.exists(f'ws_mask/amazonas/{label}'):
            fs = gcsfs.GCSFileSystem(project='pangeo-data')
            gcs_get_dir(f'pangeo-data/gross/ws_mask/amazonas/{label}', f'ws_mask/amazonas/{label}', fs)
    # get upstream basin's labels and compute its area
    # also compute upstream basins' areas
    up_labels, areas_up = {}, {}
    for label in labels_with_vs_tree[down_label]['up']:
        areas_up[label] = 0
        up_labels[label] = startswith_label(label, all_labels)
        for label2 in up_labels[label]:
            areas_up[label] += xr.open_zarr(f'ws_mask/amazonas/{label2}', auto_chunk=False)['mask'].attrs['area']
    # get downstream bassin's labels and compute its area
    down_labels = whole_labels
    for labels in up_labels.values():
        down_labels = subtract_label(labels, down_labels)
    area_down = 0
    for label in down_labels:
        area_down += xr.open_zarr(f'ws_mask/amazonas/{label}', auto_chunk=False)['mask'].attrs['area']
    areas = list(areas_up.values()) + [area_down]
    area_whole = sum(areas)
    if is_pangeo_data:
        da_p = xr.open_zarr(get_path('gs://pangeo-data/gross/ws_precipitation/amazonas'))['precipitation']
    else:
        da_p = xr.open_zarr('ws_precipitation/amazonas')['precipitation']
    
    # get whole basin's mask
    #da = get_mask('ws_mask/amazonas', whole_labels)
    #subprocess.check_call('rm -rf tmp/mask'.split())
    #da.to_dataset(name='mask').to_zarr('tmp/mask')
    # get basin's water level time series at virtual station (basin's outlet)
    he = get_waterlevel(d0, d1, labels_with_vs[down_label][0]) # there might be several stations
    dh0 = he.dropna().index[0] # first date of observation
    dh1 = he.dropna().index[-1] # last date of observation
    # start date which allows to warmup the model, but not more (warmup is in 30min)
    dh0 = max(str2datetime(d0), dh0 - timedelta(minutes=warmup*30))
    # get whole basin's precipitation and PET time series
    if False:#os.path.exists(f'tmp/precipitation/{down_label}.pkl'):
        p_whole = pd.read_pickle(f'tmp/precipitation/{down_label}.pkl')
        e_whole = pd.read_pickle(f'tmp/pet/{down_label}.pkl')
    else:
        print(f'Getting precipitation and PET for {down_label}')
        p_whole = get_precipitation(d0, d1, mask_path)
        p_whole.to_pickle(f'tmp/precipitation/{down_label}.pkl')
        e_whole = get_pet(d0, d1, 'tmp/mask')
        e_whole.to_pickle(f'tmp/pet/{down_label}.pkl')
    p_whole = da_p
    p_up, e_up = {}, {}
    # precipitation and PET of upstream bassins already exist from previous iteration
    for label in labels_with_vs_tree[down_label]['up']:
        p_up[label] = pd.read_pickle(f'tmp/precipitation/{label}.pkl')
        e_up[label] = pd.read_pickle(f'tmp/pet/{label}.pkl')
    # compute precipitation and PET of downstream bassin
    p_down = p_whole * area_whole
    e_down = e_whole * area_whole
    for label in labels_with_vs_tree[down_label]['up']:
        p_down -= p_up[label] * areas_up[label]
        e_down -= e_up[label] * areas_up[label]
    p_down /= area_whole
    e_down /= area_whole

    pe = []
    # upstream basins' precipitation and PET
    for label in labels_with_vs_tree[down_label]['up']:
        df = DataFrame()
        df['p'] = p_up[label].loc[dh0:dh1]
        df['e'] = e_up[label].loc[dh0:dh1]
        pe.append(df)
    # downstream basin's precipitation and PET
    df = DataFrame()
    df['p'] = p_down.loc[dh0:dh1]
    df['e'] = e_down.loc[dh0:dh1]
    pe.append(df)
    # basin's water level
    he = he.reindex(df.index)

    if not up_labels:
        # this is a source basin (no basin flowing into it)
        x = [dist.uniform_pdf(*r) for r in x_range]
        prior_logp = get_prior_logp(x)
        model_logp = get_likelihood_logp(gr4hh, warmup, pe, areas, he=he)
    else:
        # there are basins flowing into this basin
        x = [xp + [dist.uniform_pdf(*d_range)] for xp in x_pdf[label] for label in labels_with_vs_tree[down_label]['up']] + [dist.uniform_pdf(*r) for r in x_range]
        prior_logp = get_prior_logp(x)
        model_logp = get_likelihood_logp(gr4hh, warmup, pe, areas, he=he)
    # run SMC
    posterior, q_sims = smc.smc(x, model_logp, prior_logp, draws=draws, dask_client=client)
    plt.figure(figsize=(20, 5))
    for q_sim in q_sims:
        plt.plot(q_sim.index[warmup:], dist_map(q_sim.values[warmup:], he.h.values[warmup:]), alpha=0.005, color='blue')
    plt.scatter(he.index[warmup:], he.h.values[warmup:])
    plt.show()
    # get simulated streamflow's PDF
    if up_labels:
        # reduce model
        q_pdf = np.empty((2, n_pdf, q_sims.shape[1]))
        for i in range(q_pdf.shape[2]):
            q_pdf[:, :, i] = dist.pdf_from_samples(q_sims[:, i], nb=n_pdf, kde=True)
        pe = DataFrame()
        pe['p'] = p_whole.loc[dh0:dh1]
        pe['e'] = e_whole.loc[dh0:dh1]
        x = [dist.uniform_pdf(*r) for r in x_range]
        prior_logp = get_prior_logp(x)
        model_logp = get_likelihood_logp(gr4hh, warmup, pe, [1], q_pdf=q_pdf)
        posterior, _ = smc.smc(x, model_logp, prior_logp, draws=draws, dask_client=client)
    x_pdf[down_label] = [dist.pdf_from_samples(posterior[:, i]) for i in range(4)]