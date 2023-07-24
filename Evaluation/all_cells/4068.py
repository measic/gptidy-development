df = pd.read_csv('data.csv',
                 header=None,
                 names=['year', 'journal', 'media', 'authors', 'paper_name'],
                 usecols=['authors'])

# print df