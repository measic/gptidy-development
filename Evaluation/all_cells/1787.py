with open(os.path.join(os.environ['HOME'], 'plots_ff/model/data/frac_results_avg_ff.pkl'), 'rb') as f:
    deep_all, linear_all = pickle.load(f, encoding='latin1')

d = np.load(os.path.join(os.environ['HOME'], 'plots/ds/data/dataset_chance.npz'))
chance = d['chance_data']
training_size = d['training_size']
fracs = sorted(deep_all.keys())

output = 'plots_ff/model/data/{}_{}_hg{}_model_output.pkl'

vmax = 3.
cmax = 12.