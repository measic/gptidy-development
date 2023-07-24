ids_zero_1_count_in_last_three_week = [513, 987, 1163, 524, 397, 18, 1556, 1688, 5, 1185, 1700, 1959, 683, 1715, 958, 480, 707, 459, 1486, 1831, 722, 735, 352, 363, 1661, 1918]
for day in dateRange('2016-10-11','2016-10-31'):
    for id in ids_zero_1_count_in_last_three_week:
        if shop_info.loc[id,day] == 0:
            day_offset = (pd.to_datetime(day).date() - datetime.date(2016,10,11)).days % 7 
            rel_days = []
            for rel_day in dateRange('2016-10-11','2016-10-31'):
                if (pd.to_datetime(rel_day).date() - datetime.date(2016,10,11)).days % 7 == day_offset and rel_day != day:
                    rel_days.append(shop_info.loc[id,rel_day])
            rel_days = np.array(rel_days)
            shop_info.loc[id,day] = np.int64(rel_days.mean()+0.5)