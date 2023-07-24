default_params = {'n_trees': 10, 
                   'n_max_dim': 0,
                   'n_jobs': -1,
                   'verbose': 0,
                   'subsample_pct': .0002,
                   'ig_improvement': -np.infty
                  }

tuned_params = [{'max_depth': [2, 3, 4],
                 'min_subset': [1e-2, 1e-3, 1e-4]}]
                 

# do parameter search
ps_df = ParameterSearch(DensityForest, tuned_params, act_train[..., :3], act_val[..., :3],
                        pred_f_val.flatten(), scorer_roc_probas_df, n_iter=3, verbosity=1, n_jobs=1,
                        subsample_train=1, subsample_test=.001, default_params=default_params)

print("Testing %i combinations %i times" % (len(ps_df.combinations), ps_df.n_iter))
print(ps_df.combinations)
ps_df.fit()