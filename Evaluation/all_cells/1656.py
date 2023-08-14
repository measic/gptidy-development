plt.figure(figsize=(12,6))
fig = plt.subplot()
fig.plot(power_time_ds[400:2000], power_data_250[400:2000],  label='power',  marker='o',linewidth=0.3, markersize=1.5)
fig.legend();
fig.set_ylabel('Power [W]')
fig.set_xlabel('Time [s]')
fig.set_title('Power, moving average');