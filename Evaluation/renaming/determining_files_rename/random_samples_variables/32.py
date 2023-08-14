def basic_stock_features(input_df, mnemonic, new_time_index, inplace=False):
    variable_def = input_df.loc[mnemonic]
    if not inplace:
        variable_def = input_df.loc[mnemonic].copy()
    variable_def = variable_def.reindex(new_time_index)
    features = ['MinPrice', 'MaxPrice', 'EndPrice', 'StartPrice']
    for f in features:
        variable_def[f] = variable_def[f].fillna(method='ffill')
    features = ['TradedVolume', 'NumberOfTrades']
    for f in features:
        variable_def[f] = variable_def[f].fillna(0.0)
    variable_def['HourOfDay'] = variable_def.index.hour
    variable_def['MinOfHour'] = variable_def.index.minute
    variable_def['MinOfDay'] = variable_def.index.hour * 60 + variable_def.index.minute
    variable_def['DayOfWeek'] = variable_def.index.dayofweek
    variable_def['DayOfYear'] = variable_def.index.dayofyear
    variable_def['MonthOfYear'] = variable_def.index.month
    variable_def['WeekOfYear'] = variable_def.index.weekofyear
    variable_def['Mnemonic'] = mnemonic
    unwanted_features = ['ISIN', 'SecurityDesc', 'SecurityType', 'Currency', 'SecurityID', 'Date', 'Time', 'CalcTime']
    return variable_def.drop(unwanted_features, axis=1)