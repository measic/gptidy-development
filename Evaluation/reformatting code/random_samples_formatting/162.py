for id in [i for i in ids_no_zero_count_in_last_three_week if i in ids_cos_sim_low_3_wk_other and i in ids_stable_period_1_2_3]:
    for i in range(1,8):
        shop_info.loc[id,'wave_model_total_'+str(i)] = 0.3* shop_info.loc[id,'wave_model1_'+str(i)] + 0.7* shop_info.loc[id,'wave_model2_'+str(i)] 
        