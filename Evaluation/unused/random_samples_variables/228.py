first, last = 0, 1000 # Sample interval to plot

fig1, ax1 = plt.subplots()
ax1.plot(t[first:last], traj_data_us[first:last],  label='Angles',  marker='o',linewidth=0.3, markersize=1.5)
ax1.legend();
ax1.set_ylabel('Angles [deg]')
ax1.set_xlabel('Time')
ax1.set_title('Angles');

fig2, ax2 = plt.subplots()
ax2.plot(t[first:last], vel_us[first:last],  label='Angular velocity',  marker='o',linewidth=0.3, markersize=1.5)
ax2.legend();
ax2.set_ylabel('Angular velocity [deg/s]')
ax2.set_xlabel('Time')
ax2.set_title('Velocity');

fig3, ax3 = plt.subplots()
ax3.plot(t[first:last], acc_us[first:last],  label='Angular acceleration',  marker='o',linewidth=0.3, markersize=1.5)
ax3.legend();
ax3.set_ylabel('Angular acceleration [deg/s^2]')
ax3.set_xlabel('Time')
ax3.set_title('Acceleration');

fig4, ax4 = plt.subplots()
ax4.plot(t[first:last], np.sum(np.abs(acc_us[first:last]), axis=1),  label='Summed acc',  marker='o',linewidth=0.3, markersize=1.5)
ax4.legend();
ax4.set_ylabel('Summed accelerations [deg/s^2]')
ax4.set_xlabel('Time')
ax4.set_title('Summed accelerations');

fig5, ax5 = plt.subplots()
ax5.plot(t[first:last], psi_us[first:last],  label='Pseudo power',  marker='o',linewidth=0.3, markersize=1.5)
ax5.legend();
ax5.set_ylabel('Pseudo power [deg/s^3]')
ax5.set_xlabel('Time')
ax5.set_title('Pseudo power');

fig6, ax6 = plt.subplots()
ax6.plot(power_time_ds[first:last], power_data_250[first:last],  label='Power',  marker='o',linewidth=0.3, markersize=1.5)
ax6.legend();
ax6.set_ylabel('Power [W]')
ax6.set_xlabel('Time')
ax6.set_title('Power');