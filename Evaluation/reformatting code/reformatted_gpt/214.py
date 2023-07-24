# Load proliferation and apoptosis scores
gene_set_scores = pd.read_csv('data/gene_set_scores.csv', index_col=0)
proliferation = gene_set_scores['Cell.cycle']
apoptosis = gene_set_scores['Apoptosis']

# Apply logistic function to transform to birth rate and death rate
def logistic(x, L, k, x0=0):
    f = L / (1 + np.exp(-k * (x - x0)))
    return f

def gen_logistic(p, beta_max, beta_min, pmax, pmin, center, width):
    return beta_min + logistic(p, L=beta_max - beta_min, k=4 / width, x0=center)

def beta(p, beta_max=1.7, beta_min=0.3, pmax=1.0, pmin=-0.5, center=0.25):
    return gen_logistic(p, beta_max, beta_min, pmax, pmin, center, width=0.5)

def delta(a, delta_max=1.7, delta_min=0.3, amax=0.5, amin=-0.4, center=0.1):
    return gen_logistic(a, delta_max, delta_min, amax, amin, center, width=0.2)

birth = beta(proliferation)
death = delta(apoptosis)

# Growth rate is given by 
gr = np.exp(birth - death)
growth_rates_df = pd.DataFrame(index=gene_set_scores.index, data={'cell_growth_rate': gr})
growth_rates_df.to_csv('data/growth_gs_init.txt')