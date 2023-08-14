Start_power_indicator = 300
for i in range(len(power_data_250)):
    if power_data_250[i+10]-power_data_250[i]>Start_power_indicator:
        starting_point_power = i
        break
print('Start at power sample:',starting_point_power-1,' corresponding to time:',power_time_ds[starting_point_power-1],'sec')

Start_trajectory_indicator = 0.5
for i in range(len(traj_data_us)):
    if np.max(np.abs(acc_us[i+10]))>Start_trajectory_indicator:
        starting_point_traj = i
        break
print('Start at trajectory sample:',starting_point_traj,' corresponding to time:',t[starting_point_traj],'sec')


plt.figure(figsize=(12,6))
fig = plt.subplot()
fig.plot(power_time_ds[0:2000], power_data_250[0:2000],  label='Current',  marker='o',linewidth=0.3, markersize=1.5)
fig.plot(power_time_ds[starting_point_power-1], power_data_250[starting_point_power-1],  label='Start',  marker='o',linewidth=0.3, markersize=4)
fig.legend();
fig.set_ylabel('Ampere [W]')
fig.set_xlabel('Time')
fig.set_title('Current');

plt.figure(figsize=(12,6))
fig = plt.subplot()
fig.plot(t[0:2000], traj_data_us[0:2000],  label='Current',  marker='o',linewidth=0.3, markersize=1.5)
fig.plot(t[starting_point_traj], acc_us[starting_point_traj][0],  label='Start',  marker='o',linewidth=0.3, markersize=4)
fig.legend();
fig.set_ylabel('Ampere [W]')
fig.set_xlabel('Time')
fig.set_title('Current');