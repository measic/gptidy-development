for i in range(1,8):
    shop_info.loc[:,'wave_model_total_'+str(i)] = shop_info['ratio'] * shop_info.loc[:,'wave_model_total_'+str(i)]