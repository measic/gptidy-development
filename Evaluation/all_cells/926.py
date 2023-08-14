filename="/Users/shengyuchen/Dropbox/Engagement - Business/My Hub/AI:ML:DL Playground/Local Python/AI-ML-DL Algorithms/LSTM Neural Networks/shampoo-sales.csv"
def parser(x):
    return datetime.strptime('190'+x, '%Y-%b') # String manpuation
series=read_csv(filename, header=0,parse_dates=[0],index_col=0,squeeze=True)

# If the parsed data only contains one column then return a Series
