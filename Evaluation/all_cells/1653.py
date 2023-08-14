n_phases   = 3   #Number of phases in measured data
power_data = np.ndarray((len(Volt_Amp_data),1))
power_time = np.ndarray((len(Volt_Amp_data),1))
amp_data   = np.ndarray((len(Volt_Amp_data),n_phases))
volt_data  = np.ndarray((len(Volt_Amp_data),n_phases))

for i, sample in enumerate(Volt_Amp_data):
    power_time[i] = sample[0]
    volt_data[i]  = np.array([sample[1], sample[2], sample[3]])
    amp_data[i]   = np.array([sample[4], sample[5], sample[6]])
    power_data[i] = np.abs(sample[1]*sample[4]) \
        + np.abs(sample[2]*sample[5]) \
        + np.abs(sample[3]*sample[6]) 
