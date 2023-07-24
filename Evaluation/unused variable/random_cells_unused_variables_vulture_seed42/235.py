n_periods = 0 # Where to start the plot in number of periods
period    = 200  # Number of samples in a period (Voltage_Current_sample_freq)/50Hz
interval  = 2    # Number of periods to be plotted
phase     = 0    # Which phase to be plotted (0 --> phase1, 1 --> phase2, 2 --> phase3)
amp_scale = 100  # Which factor to use to scale up the current data in the plot

plt.figure(figsize=(12,6))
fig = plt.subplot()
x = range(len(power_data))
fig.plot(power_time[n_periods*period:(n_periods+interval)*period], amp_data[n_periods*period:(n_periods+interval)*period,phase]*amp_scale,  label='amp',  marker='o',linewidth=0.3, markersize=1.5)
fig.plot(power_time[n_periods*period:(n_periods+interval)*period], volt_data[n_periods*period:(n_periods+interval)*period,phase],  label='volt',  marker='o',linewidth=0.3, markersize=1.5)
fig.plot(power_time[n_periods*period:(n_periods+interval)*period], power_data[n_periods*period:(n_periods+interval)*period],  label='power',  marker='o',linewidth=0.3, markersize=1.5)
fig.legend();
fig.set_ylabel('Power [W]')
fig.set_xlabel('Time [s]')
fig.set_title('Total Power');