def fillna_double_12(x):
    if pd.to_datetime(x['start_day']).date() < pd.to_datetime('2015-12-12').date():  
        if x['2015-12-05']>0 and x['2015-12-19']>0 :
            return int(x['2015-12-05'] + x['2015-12-19'] /2.0 +0.5)
        elif x['2015-12-05']>0: return x['2015-12-05']
        elif x['2015-12-19']>0: return x['2015-12-19']
        else: return 0
    return 0
shop_info['2015-12-12'] = shop_info.apply(lambda x:fillna_double_12(x),axis=1)