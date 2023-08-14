with open(os.path.join(os.environ['HOME'], 'plots/model/data/frac_results.pkl'), 'rb') as f:
    deep_all, linear_all, _ = pickle.load(f, encoding='latin1')

d = np.load(os.path.join(os.environ['HOME'], 'plots/ds/data/dataset_chance.npz'))
chance = d['chance_data']
training_size = d['training_size']
fracs = sorted(deep_all.keys())

output = 'plots/model/data/{}_{}_hg_a{}_model_output.pkl'

vmax = 2.8
cmax = 9.2

vmax = 3.
cmax = 12.