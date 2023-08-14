for i in range(1,8):
    for id in ids_cos_sim_high_3_wk:       
        shop_info.loc[id,'wave_model_total_'+str(i)] = shop_info.loc[id,'wave_model1_'+str(i)]
#print shop_info.loc[ids_cos_sim_high_3_wk,'wave_model_total_1':'wave_model_total_7']