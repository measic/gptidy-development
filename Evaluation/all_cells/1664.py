temp = pd.read_excel(temp_data_path)
temp = temp.values
temp_data = temp[0][3:]

n_timesteps = len(traj_data_synced)
num_joints=6
temp_lin_int = np.ndarray((n_timesteps,num_joints))
for i in range(num_joints):
    temp_lin_int[0:,i] = np.linspace(temp_data[0+i],temp_data[6+i],num=n_timesteps)