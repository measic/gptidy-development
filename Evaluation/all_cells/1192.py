ids_no_zero_count_in_last_three_week = [i for i in shop_info.index.tolist() if i not in ids_zero_morethan1_count_in_last_three_week and i not in  ids_cos_sim_high_3_wk]