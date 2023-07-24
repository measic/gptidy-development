for id in ids_zero_morethan1_count_in_last_three_week_and_two_week:
    if id in ids_stable_period_1_2_3:
        for i in range(1,8):
            shop_info.loc[id,'wave_model_total_'+str(i)] = shop_info.loc[id,'wave_model2_'+str(i)]
    else: # 最好根据相似商家融合
        for i in range(1,8):
            shop_info.loc[id,'wave_model_total_'+str(i)] = shop_info.loc[id,'wave_model1_'+str(i)]
        