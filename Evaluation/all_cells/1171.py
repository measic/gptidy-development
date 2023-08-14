def cal_start_day(x):
    for day in dateRange('2015-07-01','2016-10-31'):
        if x[day]>0 :
            return day
    

shop_info['start_day'] = shop_info.apply(lambda x:cal_start_day(x),axis =1)