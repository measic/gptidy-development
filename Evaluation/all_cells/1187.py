def cal_wave_range(x):
    sales_count = sorted(x['2016-10-11':'2016-10-31'].tolist())
    if sum(sales_count[18:]) == 0 :return 0
    return (sum(sales_count[18:]) - sum(sales_count[:3]))/float(sum(sales_count[18:]))
shop_info['wave_range'] = shop_info.apply(lambda x: cal_wave_range(x),axis = 1)