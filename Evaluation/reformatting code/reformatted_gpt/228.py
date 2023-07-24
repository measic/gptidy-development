for id in [i for i in ids_no_zero_count_in_last_three_week if i in ids_cos_sim_high_23_wk and i in ids_no_stable_period]:
    for i in range(1, 8):
        shop_info.loc[id, 'wave_model_total_' + str(i)] = shop_info.loc[id, 'wave_model1_' + str(i)]