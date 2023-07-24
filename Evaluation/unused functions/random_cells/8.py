def create_xgb_target (df):
    return df.MaxPrice.shift(-1).fillna (method='ffill')