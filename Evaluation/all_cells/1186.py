ids_low_count_in_last_3_wk = shop_info[shop_info.loc[:,'2016-10-11':'2016-10-31'].mean(axis=1)<50].index.tolist()
print len(ids_low_count_in_last_3_wk)
#draw_ids(ids_low_count_in_last_3_wk[:5],start_date='2016-02-11',end_date='2016-10-31',by_week=True)