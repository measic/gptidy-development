start_day = (pd.to_datetime('2016-11-01').date() - datetime.timedelta(14)).strftime("%Y-%m-%d")
for id in ids_zero_morethan1_count_in_last_three_week_but_no_zero_in_last_two_week:
    for day_number in range(1, 8):  # 1~7
        predict_day = '2016-11-' + '%02d' % day_number
        predict_day = pd.to_datetime(predict_day).date()
        day_list = [day for day in dateRange(start_day, '2016-10-31') if (predict_day - pd.to_datetime(day).date()).days % 7 == 0]
        shop_info.loc[id, 'wave_model1_' + str(day_number)] = shop_info.loc[id, day_list].mean()

    if id in ids_stable_period_1_2_3:
        for i in range(1, 8):
            shop_info.loc[id, 'wave_model_total_' + str(i)] = 0.5 * shop_info.loc[id, 'wave_model1_' + str(i)] + 0.5 * shop_info.loc[id, 'wave_model2_' + str(i)]

    else:
        for i in range(1, 8):
            shop_info.loc[id, 'wave_model_total_' + str(i)] = shop_info.loc[id, 'wave_model1_' + str(i)]