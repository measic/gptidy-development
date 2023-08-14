B2_NTOT_WINTER_SETTINGS = lv_workspace.get_subset_object('B').get_step_object('step_2').indicator_ref_settings['ntot_winter']
lv_workspace.get_subset_object('B').get_step_object('step_2').indicator_ref_settings['ntot_winter'].allowed_variables
# gör om till
# lv_workspace.get_indicator_ref_settings(step = , subset = , indicator = , waterbody/type)
# ger samma resultat som:
#lv_workspace.get_subset_object('B').get_step_object('step_2').indicator_ref_settings['ntot_winter'].settings.ref_columns

lv_workspace.get_subset_object('B').get_step_object('step_2').indicator_ref_settings['ntot_winter'].settings.get_value('EK G/M', 22)
#print(B2_NTOT_WINTER_SETTINGS)
#B2_NTOT_WINTER_SETTINGS.get_value('2', 'DEPTH_INTERVAL')