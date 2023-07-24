column_filter = ['ISIN', 'Mnemonic', 'SecurityDesc', 'SecurityType', 'Currency', 'SecurityID', 'Date', 'Time', 'StartPrice', 'MaxPrice', 'MinPrice', 'EndPrice', 'TradedVolume', 'NumberOfTrades']
n_df = df[column_filter]
if not inplace:
    n_df = df.copy ()

n_df.drop (n_df.Time == 'Time', inplace = True)
# we want the dates to be comparable to datetime.strptime()
n_df["CalcTime"] = pd.to_datetime("1900-01-01 " + n_df["Time"], errors='coerce')
n_df["CalcDateTime"] = pd.to_datetime(n_df["Date"] + " " + n_df["Time"], errors='coerce')

# Filter common stock
# Filter between trading hours 08:00 and 20:00
# Exclude auctions (those are with TradeVolume == 0)
only_common_stock = n_df[n_df.SecurityType == 'Common stock']
time_fmt = "%H:%M"
opening_hours_str = "08:00"
closing_hours_str = "20:00"
opening_hours = datetime.strptime(opening_hours_str, time_fmt)
closing_hours = datetime.strptime(closing_hours_str, time_fmt)

cleaned_common_stock = only_common_stock[(only_common_stock.TradedVolume > 0) & \
                  (only_common_stock.CalcTime >= opening_hours) & \
                  (only_common_stock.CalcTime <= closing_hours)]

bymnemonic = cleaned_common_stock[['Mnemonic', 'TradedVolume']].groupby(['Mnemonic']).sum()
number_of_stocks = 100
top = bymnemonic.sort_values(['TradedVolume'], ascending=[0]).head(number_of_stocks)
top_k_stocks = list(top.index.values)
cleaned_common_stock = cleaned_common_stock[cleaned_common_stock.Mnemonic.isin(top_k_stocks)]
sorted_by_index = cleaned_common_stock.set_index(['Mnemonic', 'CalcDateTime']).sort_index()
non_empty_days = sorted(list(cleaned_common_stock['Date'].unique()))
new_datetime_index = build_index(non_empty_days, opening_hours_str, closing_hours_str)["OrganizedDateTime"].values

stocks = []
for stock in top_k_stocks:
    stock = basic_stock_features(sorted_by_index, stock, new_datetime_index, inplace=True)
    stocks.append(stock)
# prepared should contain the numeric features for all top k stocks,
# for all days in the interval, for which there were trades (that means excluding weekends and holidays)
# for all minutes from 08:00 until 20:00
# in minutes without trades the prices from the last available minute are carried forward
# trades are filled with zero for such minutes
# a new column called HasTrade is introduced to denote the presence of trades
prepared = pd.concat(stocks, axis=0).dropna(how='any')
prepared.Mnemonic = prepared.Mnemonic.astype('category')
return prepared