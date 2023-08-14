ids_highest_point_error_compared_to_last_three_days = []
def cal_highest_point_error_compared_to_last_three_days(x):
    sales_list = sorted(x['2016-10-11':'2016-10-31'].tolist(),reverse=True)
    if sales_list[1] > 0:
        if 1.0 * sales_list[0] / sales_list[1] > 1.2:
            ids_highest_point_error_compared_to_last_three_days.append(x['shop_id'])
shop_info.apply(lambda x: cal_highest_point_error_compared_to_last_three_days(x) ,axis=1)
print len(ids_highest_point_error_compared_to_last_three_days)
#draw_ids(ids_highest_point_error_compared_to_last_three_days,start_date='2016-10-11',end_date='2016-10-31',by_week=True)