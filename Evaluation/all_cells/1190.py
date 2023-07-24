ids_cos_sim_low_between_wk_1_2 = shop_info[shop_info['cos_sim_between_wk_1_2']<0.98].index.tolist()
ids_cos_sim_low_between_wk_2_3 = shop_info[shop_info['cos_sim_between_wk_2_3']<0.98].index.tolist()
ids_cos_sim_low_between_wk_1_3 = shop_info[shop_info['cos_sim_between_wk_1_3']<0.98].index.tolist()
ids_cos_sim_low_3_wk = []
ids_cos_sim_low_3_wk.extend(ids_cos_sim_low_between_wk_1_2)
ids_cos_sim_low_3_wk.extend(ids_cos_sim_low_between_wk_2_3)
ids_cos_sim_low_3_wk.extend(ids_cos_sim_low_between_wk_1_3)
ids_cos_sim_low_3_wk = list(set(ids_cos_sim_low_3_wk))
print len(ids_cos_sim_low_between_wk_1_2)
print len(ids_cos_sim_low_between_wk_2_3)
print len(ids_cos_sim_low_between_wk_1_3)
print len(ids_cos_sim_low_3_wk)
ids_cos_sim_high_3_wk =[ i  for i in shop_info.index.tolist() if i not in ids_cos_sim_low_3_wk]
print len(ids_cos_sim_high_3_wk)
ids_cos_sim_high_23_wk = [i for i in shop_info[shop_info['cos_sim_between_wk_2_3']>0.98].index.tolist() if i not in ids_cos_sim_high_3_wk and i in  shop_info[shop_info['cos_sim_between_wk_1_2']>0.95].index.tolist()]
print len(ids_cos_sim_high_23_wk)

ids_cos_sim_low_3_wk_other = [i for i in ids_cos_sim_low_3_wk if i not in ids_cos_sim_high_23_wk]
print len(ids_cos_sim_low_3_wk_other)