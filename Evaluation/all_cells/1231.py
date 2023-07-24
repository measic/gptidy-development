for i in range(1,15):
    shop_info.loc[:,'predict_day_'+str(i)] = shop_info.loc[:,'predict_day_'+str(i)].apply(lambda x : int(x+0.5))
    