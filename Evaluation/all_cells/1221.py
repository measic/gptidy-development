for i in range(1,15):
    if i <= 7:
        shop_info.loc[:,'predict_day_'+str(i)] = shop_info.loc[:,'wave_model_total_'+str(i)]
    else:
        shop_info.loc[:,'predict_day_'+str(i)] = shop_info.loc[:,'wave_model_total_'+str(i-7)]