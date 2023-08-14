start_day = (pd.to_datetime('2016-11-01').date() - datetime.timedelta(21)).strftime("%Y-%m-%d") 
for day_number in range(1,8): # 1~7
    
    predict_day = '2016-11-'+'%02d' %  day_number
    predict_day = pd.to_datetime(predict_day).date()
    day_list = [day for day in dateRange(start_day,'2016-10-31') if (predict_day - pd.to_datetime(day).date()).days % 7 == 0]
    shop_info.loc[ids_cos_sim_low_3_wk_other,'wave_model1_'+str(day_number)] = shop_info.loc[ids_cos_sim_low_3_wk_other,day_list].mean(axis=1)

#shop_info['wave_model1_1']