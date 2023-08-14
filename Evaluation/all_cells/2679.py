temp_model_21 = []
temp_model_25 = []
temp_model_27 = []
temp_grads_21 = []
temp_grads_25 = []
temp_grads_27 = []

with open ("mu_test_data/diff_mu_logL=2_1231_model") as model_21:
    data_cleanup(model_21,temp_model_21)
with open ("mu_test_data/diff_mu_logL=2_5001_model") as model_25:
    data_cleanup(model_25,temp_model_25)
with open ("mu_test_data/diff_mu_logL=2_1231_model") as model_27:
    data_cleanup(model_27,temp_model_27)
model_data_21 = np.array(temp_model_21)
model_data_25 = np.array(temp_model_25)
model_data_27 = np.array(temp_model_27)

with open ("mu_test_data/diff_mu_logL=2_1231_grads") as grads_21:
    data_cleanup(grads_21,temp_grads_21)
with open ("mu_test_data/diff_mu_logL=2_5001_grads") as grads_25:
    data_cleanup(grads_25,temp_grads_25)
with open ("mu_test_data/diff_mu_logL=2_1231_grads") as grads_27:
    data_cleanup(grads_27,temp_grads_27)
grads_data_21 = np.array(temp_grads_21)
grads_data_25 = np.array(temp_grads_25)
grads_data_27 = np.array(temp_grads_27)

focus_model_21 = focus_sync(grads_data_21,model_data_21)
focus_model_25 = focus_sync(grads_data_25,model_data_25)
focus_model_27 = focus_sync(grads_data_27,model_data_27)

del_mu_21 = grads_data_21[:,4]
del_mu_25 = grads_data_25[:,4]
del_mu_27 = grads_data_27[:,4]

rad_ad_21 = focus_model_21[:,10] - focus_model_21[:,11]
rad_ad_25 = focus_model_25[:,10] - focus_model_25[:,11]
rad_ad_27 = focus_model_27[:,10] - focus_model_27[:,11]

D_21 = grads_data_21[:,-2]
D_25 = grads_data_25[:,-2]
D_27 = grads_data_27[:,-2]

rad_frac_21 = focus_model_21[:,1]
rad_frac_25 = focus_model_25[:,1]
rad_frac_27 = focus_model_27[:,1]

mass_frac_21 = grads_data_21[:,0]
mass_frac_25 = grads_data_25[:,0]
mass_frac_27 = grads_data_27[:,0]

logP_21 = focus_model_21[:,2]
logP_25 = focus_model_25[:,2]
logP_27 = focus_model_27[:,2]

logT_21 = focus_model_21[:,3]
logT_25 = focus_model_25[:,3]
logT_27 = focus_model_27[:,3]

logDens_21 = focus_model_21[:,4]
logDens_25 = focus_model_25[:,4]
logDens_27 = focus_model_27[:,4]

opac_21 = focus_model_21[:,12]
opac_25 = focus_model_25[:,12]
opac_27 = focus_model_27[:,12]

mu_21 = grads_data_21[:,1]
mu_25 = grads_data_25[:,1]
mu_27 = grads_data_27[:,1]

model_degen_21 = data_focus(mu_21,0.134e1, model_data_21)
model_degen_25 = data_focus(mu_25,0.134e1, model_data_25)
model_degen_27 = data_focus(mu_27,0.134e1, model_data_27)