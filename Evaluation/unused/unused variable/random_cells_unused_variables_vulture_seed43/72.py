ae = auto_encoder(m=m, ls=ls, ld=ld, le=le, lg=lg, rtol=rtol, xtol=None, N_inner=N_inner, N_outer=N_outer)
tstart = time.time()
Z = ae.fit_transform(X, L)
time_features = time.time() - tstart
print('Elapsed time: {:.0f} seconds'.format(time_features))