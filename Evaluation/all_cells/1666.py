feature_dim = len(traj_data_synced[0])*4 + 1

aug_input_norm = np.ndarray((len(traj_data_synced),feature_dim))
traj_data_norm = np.ndarray(np.shape(traj_data_synced))
vel_norm = np.ndarray(np.shape(vel_synced))
acc_norm = np.ndarray(np.shape(acc_synced))
psi_norm = np.ndarray(np.shape(psi_synced))
temp_norm = np.ndarray(np.shape(temp_lin_int))

A1_constraint = [np.deg2rad(-185), np.deg2rad(185)]
A2_constraint = [np.deg2rad(-135), np.deg2rad(35)]
A3_constraint = [np.deg2rad(-120), np.deg2rad(158)]
A4_constraint = [np.deg2rad(-350), np.deg2rad(350)]
A5_constraint = [np.deg2rad(-119), np.deg2rad(119)]
A6_constraint = [np.deg2rad(-350), np.deg2rad(350)]

vel_max = 4.159647569601188
vel_min = -3.9450433392170803
acc_max = 27.338764681179683
acc_min = -28.319179147808107
psi_max = 126.43383111466377
psi_min = 0.0
temp_max = 340
temp_min = 285

constraints_min = [A1_constraint[0],A2_constraint[0],A3_constraint[0],A4_constraint[0],A5_constraint[0],A6_constraint[0]]
constraints_diff = [float(np.diff(A1_constraint)), float(np.diff(A2_constraint)),float(np.diff(A3_constraint)),float(np.diff(A4_constraint)),float(np.diff(A5_constraint)),float(np.diff(A6_constraint))]

vel_diff = vel_max - vel_min
acc_diff = acc_max - acc_min
psi_diff = psi_max - psi_min
temp_diff = temp_max - temp_min

for i in range(len(traj_data_synced)):
    traj_data_norm[i] = 2*np.divide((traj_data_synced[i] - constraints_min),constraints_diff) - 1
    vel_norm[i] = 2*(vel_synced[i] - vel_min)/vel_diff - 1
    acc_norm[i] = 2*(acc_synced[i] - acc_min)/acc_diff - 1
    psi_norm[i] = psi_synced[i]/psi_diff    
    temp_norm[i] = 2*(temp_lin_int[i] - temp_min)/temp_diff - 1
    aug_input_norm[i] = np.concatenate((traj_data_norm[i], vel_norm[i], acc_norm[i], psi_norm[i], temp_norm[i]), axis=None)

with open(data_path + '/augmented_normalized_input.pickle', 'wb') as file:
    pickle.dump(aug_input_norm, file)
    file.close()