for day_number in range(1,8): # 1~7
    shop_info.loc[:,'wave_model2_'+str(day_number)] = 0.0
def get_avg_from_stable_period_(id,n):
    wks = shop_info.loc[id,'stable_period_'+str(n)]
    day_list = []
    for wk_pair in wks:
        wk_start_date = week_to_date(wk_pair[0])[0]
        wk_end_date = week_to_date(wk_pair[1])[1]
        day_list.extend(dateRange(wk_start_date,wk_end_date))
    #print day_list
    #print len(day_list)
    if len(day_list) % 7 != 0 : print 'ERROR'
    #week_number = len(day_list)/7
    for day_number in range(1,8): # 1~7
        predict_day = '2016-11-'+'%02d' %  day_number
        predict_day = pd.to_datetime(predict_day).date()
        train_day_list = [day for day in day_list if (predict_day - pd.to_datetime(day).date()).days % 7 == 0]
        #print train_day_list
        shop_info.loc[id,'wave_model2_'+str(day_number)] =  shop_info.loc[id,train_day_list].mean()     

for id in ids_stable_period_1:
    get_avg_from_stable_period_(id,1)
for id in ids_stable_period_2:
    get_avg_from_stable_period_(id,2)
for id in ids_stable_period_3:
    get_avg_from_stable_period_(id,3)
        
