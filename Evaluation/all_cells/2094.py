import numpy as np

np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))