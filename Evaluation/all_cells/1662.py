fig1, ax1 = plt.subplots()
ax1.plot(t_synced[0:1000], power_data_synced[0:1000],  label='Power',  marker='o',linewidth=0.3, markersize=1.5)
ax1.legend();
ax1.set_ylabel('Power [W]')
ax1.set_xlabel('Time')
ax1.set_title('Power');

fig2, ax2 = plt.subplots()
ax2.plot(t_synced[0:1000], traj_data_synced[0:1000],  label='Angles',  marker='o',linewidth=0.3, markersize=1.5)
ax2.legend();
ax2.set_ylabel('Angles [deg]')
ax2.set_xlabel('Time')
ax2.set_title('Angles');