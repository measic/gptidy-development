tickers = ["IBM", "AAPL", "GOOGL", "MSFT"]

data = quandl.get_table(
    "WIKI/PRICES",
    ticker=tickers,
    qopts={"columns": ["date", "ticker", "adj_close"]},
    date={
        "gte": "2015-1-1",
        "lte": "2017-12-31"
    },
    paginate=True,
)

dataframe = data.set_index("date")
dataframe = dataframe.pivot(columns="ticker")
print("{}\n".format(dataframe.columns))
dataframe.columns = [col[1] for col in dataframe.columns]
print("{}".format(dataframe.columns))
dataframe = pd.DataFrame(dataframe)
dataframe = dataframe.dropna()
display.display(dataframe.head(10))