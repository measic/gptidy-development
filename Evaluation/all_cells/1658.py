US = 3 #Upsample factor
traj_data_us = np.ndarray((len(traj_data)*US,6))
vel_us = np.ndarray(np.shape(traj_data_us))
acc_us = np.ndarray(np.shape(traj_data_us))
psi_us = np.ndarray((len(traj_data)*US,1))
k=0
for i, angles in enumerate(traj_data[0:-1]):
    for j in range(len(angles)):
        a = traj_data[i][j]
        b = traj_data[i+1][j]
        lin_in = np.linspace(a,b,num=US)
        traj_data_us[k:k+US,j] = lin_in
        
        a = vel[i][j]
        b = vel[i+1][j]
        lin_in = np.linspace(a,b,num=US)
        vel_us[k:k+US,j] = lin_in

        a = acc[i][j]
        b = acc[i+1][j]
        lin_in = np.linspace(a,b,num=US)
        acc_us[k:k+US,j] = lin_in
        
    a = psi[i]
    b = psi[i+1]
    lin_in = np.linspace(a,b,num=US).reshape(US,1)
    psi_us[k:k+US] = lin_in
        
    k+=US
    
#Time vector for angle measurements (fixed in KUKA system)
delta_t = 0.012/US
t = np.ndarray((len(traj_data_us),1))
t[0] = 0
for i in range(1,len(traj_data_us)):
    t[i] = t[i-1] + delta_t