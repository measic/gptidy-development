# result_dir = '/Users/nishant/ray_results/2018-08-26_22-43-29r4a9tt7u'
result_dir = '/Users/nishant/ray_results/2018-08-28_22-18-1581dc8109'
fname = result_dir + '/iter_vars.pkl'
with open(fname, 'rb') as file:
    itervars = pickle.load(file)