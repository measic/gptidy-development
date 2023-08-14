start_day = (pd.to_datetime('2016-11-01').date() - datetime.timedelta(21)).strftime("%Y-%m-%d") 
for day_number in range(1,8): # 1~7
    #shop_info.loc[:,'wave_model1_'+str(day_number)] = 0.0
    predict_day = '2016-11-'+'%02d' %  day_number
    predict_day = pd.to_datetime(predict_day).date()
    day_list = [day for day in dateRange(start_day,'2016-10-31') if (predict_day - pd.to_datetime(day).date()).days % 7 == 0]
    for id in ids_cos_sim_high_23_wk:
        shop_info.loc[id,'wave_model1_'+str(day_number)] = (2*shop_info.loc[id,day_list][0]+5*shop_info.loc[id,day_list][1]+5*shop_info.loc[id,day_list][2])/12.0
    