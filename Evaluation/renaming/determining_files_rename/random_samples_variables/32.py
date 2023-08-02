def basic_stock_features(input_df, mnemonic, new_time_index, inplace=False):
    stock = input_df.loc[mnemonic]
    if not inplace:
        stock = input_df.loc[mnemonic].copy()
    stock = stock.reindex(new_time_index)
    variable_def = ['MinPrice', 'MaxPrice', 'EndPrice', 'StartPrice']
    for f in variable_def:
        stock[f] = stock[f].fillna(method='ffill')
    variable_def = ['TradedVolume', 'NumberOfTrades']
    for f in variable_def:
        stock[f] = stock[f].fillna(0.0)
    stock['HourOfDay'] = stock.index.hour
    stock['MinOfHour'] = stock.index.minute
    stock['MinOfDay'] = stock.index.hour * 60 + stock.index.minute
    stock['DayOfWeek'] = stock.index.dayofweek
    stock['DayOfYear'] = stock.index.dayofyear
    stock['MonthOfYear'] = stock.index.month
    stock['WeekOfYear'] = stock.index.weekofyear
    stock['Mnemonic'] = mnemonic
    unwanted_features = ['ISIN', 'SecurityDesc', 'SecurityType', 'Currency', 'SecurityID', 'Date', 'Time', 'CalcTime']
    return stock.drop(unwanted_features, axis=1)