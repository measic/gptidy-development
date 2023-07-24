#load data
#parse the date to datetime format
#set index to date

df = pd.read_csv(os.path.join(dir, file), parse_dates=['Date'], index_col='Date')
df[:5].T