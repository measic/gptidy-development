def cal_cos_sim(x,start_day_of_week,end_day_of_week,start_day_of_next_week,end_day_of_next_week):
    wka_vec =  np.array(x[start_day_of_week:end_day_of_week].tolist())
    wkb_vec =  np.array(x[start_day_of_next_week:end_day_of_next_week].tolist())
    sim = wka_vec.dot(wkb_vec) / (np.sqrt(np.sum(np.square(wka_vec))) * np.sqrt(np.sum(np.square(wkb_vec))))
    return sim 
    
    
total_day = pd.to_datetime('2016-11-01').date()-pd.to_datetime('2015-07-01').date() 
total_day = total_day.days
total_week = total_day / 7
start_day = pd.to_datetime('2015-07-07').date()
for week_number in range(total_week-1): # 0 ~ 68-1
    start_day_of_week = start_day +  datetime.timedelta(week_number*7) 
    end_day_of_week = start_day_of_week + datetime.timedelta(6)
    start_day_of_next_week = start_day_of_week + datetime.timedelta(7)
    end_day_of_next_week = end_day_of_week + datetime.timedelta(7)
    start_day_of_week = start_day_of_week.strftime("%Y-%m-%d")
    end_day_of_week = end_day_of_week.strftime("%Y-%m-%d")
    start_day_of_next_week = start_day_of_next_week.strftime("%Y-%m-%d")
    end_day_of_next_week = end_day_of_next_week.strftime("%Y-%m-%d")
    shop_info['cos_sim_wk_'+str(week_number)] = shop_info.apply(lambda x: cal_cos_sim(x,start_day_of_week,end_day_of_week,start_day_of_next_week,end_day_of_next_week),axis=1)