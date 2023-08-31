def function_def(df, horizon, inplace=False):
    n_df = df
    if not inplace:
        n_df = df.copy()
    for offset in range(1, horizon + 1):
        min_price = n_df['MinPrice'].shift(offset).fillna(method='bfill')
        max_price = n_df['MaxPrice'].shift(offset).fillna(method='bfill')
        start_price = n_df['StartPrice'].shift(offset).fillna(method='bfill')
        end_price = n_df['EndPrice'].shift(offset).fillna(method='bfill')
        trade_vol = n_df['TradedVolume'].shift(offset).fillna(method='bfill')
        num_trades = n_df['NumberOfTrades'].shift(offset).fillna(method='bfill')
        n_df['h{}_MinPrice'.format(offset)] = min_price
        n_df['h{}_MaxPrice'.format(offset)] = max_price
        n_df['h{}_StartPrice'.format(offset)] = start_price
        n_df['h{}_EndPrice'.format(offset)] = end_price
        n_df['h{}_TradeVolume'.format(offset)] = trade_vol
        n_df['h{}_NumberOfTrades'.format(offset)] = num_trades
    return n_df