# Test and training set
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
# Combine into one dataset for the purposes of cleaning, and make sure that index continues
data_full = pd.concat([train, test], keys = ['train', 'test'])#ignore_index = True)