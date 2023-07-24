#Align the data
traj_data_synced = traj_data_us[starting_point_traj:-1]
vel_synced = vel_us[starting_point_traj:-1]
acc_synced = acc_us[starting_point_traj:-1]
psi_synced = psi_us[starting_point_traj:-1]
power_data_synced = power_data_250[starting_point_power-1:starting_point_power-1+len(traj_data_synced)]
t_synced = t[starting_point_traj:-1]