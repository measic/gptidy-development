def function_def(df):
    return df.MaxPrice.shift(-1).fillna(method='ffill')