if not os.path.exists('../data/amazonas/amazonas.pkl'):
    df_vs = locate_vs('../data/amazonas/amazonas.txt', pix_nb=20, acc_min=1_000_000)
    df_vs.to_pickle('../data/amazonas/amazonas.pkl')
else:
    df_vs = pd.read_pickle('../data/amazonas/amazonas.pkl')