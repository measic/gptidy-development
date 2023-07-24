dcv_acc = deep_all[fracs[-1]][:, 2] * 100.
lcv_acc = linear_all[fracs[-1]][:, 2] * 100.
cv_chance = chance[0, :, -1].mean(axis=-1) * 100.
dcv_cc = np.zeros(4)
dcv_ncc = np.zeros(4)
lcv_cc = np.zeros(4)
lcv_ncc = np.zeros(4)

dc_acc = other_deep_accuracy['c'][:, 2] * 100.
lc_acc = other_linear_accuracy['c'][:, 2] * 100.
c_chance = chance[1, :, -1].mean(axis=-1) * 100.
dc_cc = np.zeros(4)
dc_ncc = np.zeros(4)
lc_cc = np.zeros(4)
lc_ncc = np.zeros(4)

dv_acc = other_deep_accuracy['v'][:, 2] * 100.
lv_acc = other_linear_accuracy['v'][:, 2] * 100.
v_chance = chance[2, :, -1].mean(axis=-1) * 100.
dv_cc = np.zeros(4)
dv_ncc = np.zeros(4)
lv_cc = np.zeros(4)
lv_ncc = np.zeros(4)

for ii, s in enumerate(subjects):
    print(deep_cv_mats[s].shape)
    dcv_cc[ii] = accuracy.channel_capacity(deep_cv_mats[s].mean(axis=0))
    dcv_ncc[ii] = accuracy.naive_channel_capacity(dcv_acc[ii].mean()/100., deep_cv_mats[s].shape[-1]+1)
    lcv_cc[ii] = accuracy.channel_capacity(linear_cv_mats[s].mean(axis=0))
    lcv_ncc[ii] = accuracy.naive_channel_capacity(lcv_acc[ii].mean()/100., linear_cv_mats[s].shape[-1]+1)
    
    dc_cc[ii] = accuracy.channel_capacity(deep_c_mats[s].mean(axis=0))
    dc_ncc[ii] = accuracy.naive_channel_capacity(dc_acc[ii].mean()/100., deep_c_mats[s].shape[-1]+1)
    lc_cc[ii] = accuracy.channel_capacity(linear_c_mats[s].mean(axis=0))
    lc_ncc[ii] = accuracy.naive_channel_capacity(lc_acc[ii].mean()/100., linear_c_mats[s].shape[-1]+1)
    
    dv_cc[ii] = accuracy.channel_capacity(deep_v_mats[s].mean(axis=0))
    dv_ncc[ii] = accuracy.naive_channel_capacity(dv_acc[ii].mean()/100., deep_v_mats[s].shape[-1]+1)
    lv_cc[ii] = accuracy.channel_capacity(linear_v_mats[s].mean(axis=0))
    lv_ncc[ii] = accuracy.naive_channel_capacity(lv_acc[ii].mean()/100., linear_v_mats[s].shape[-1]+1)