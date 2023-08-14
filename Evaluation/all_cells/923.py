

# Load dataset and writing the custom parser
def parser(x):
    return datetime.strptime(x, '%m/%d/%y')

# Man gotta figure out the strptime function to see how it actually works 

# Date_parser always get called to pass a function understand the dates
series=read_csv("/Users/shengyuchen/Dropbox/Engagement - Business/My Hub/AI:ML:DL Playground/Local Python/AI-ML-DL Algorithms/LSTM Neural Networks/shampoo-sales.csv",header=0,parse_dates=[0],index_col=0,squeeze=True,date_parser=parser)
series.head()
