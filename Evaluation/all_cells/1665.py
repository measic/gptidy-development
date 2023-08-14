#Create the augmented input vector containing [angle1,..,angle6, vel1,..,vel6, acc1,..,acc6, psi] for all timesteps.

aug_feature_dim = 25
aug_input = np.ndarray((len(traj_data_synced),aug_feature_dim))

for i in range(len(traj_data_synced)):
    aug_input[i] = np.concatenate((traj_data_synced[i], vel_synced[i], acc_synced[i], psi_synced[i], temp_lin_int[i]), axis=None)

with open(data_path + '/augmented_input.pickle', 'wb') as file:
    pickle.dump(aug_input, file)
    file.close()