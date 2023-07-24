#Time vector for angle measurements (fixed in KUKA system)
delta_t = 0.012
t = np.ndarray((len(traj_data),1))
t[0] = 0
for i in range(1,len(traj_data)):
    t[i] = t[i-1] + delta_t

#Velocity 
vel = np.ndarray(np.shape(traj_data))
for i in range(len(traj_data)-1):
    vel[i] = np.divide( traj_data[i+1] - traj_data[i], delta_t)
vel[-1] = vel[-2]

#Acceleration
acc = np.ndarray(np.shape(traj_data))
for i in range(len(traj_data)-1):
    acc[i] = np.divide( vel[i+1] - vel[i], delta_t)
acc[-1] = acc[-2]

#Pseudopower
psi = np.ndarray((np.shape(traj_data)[0],1))
for i in range(len(traj_data)):
    psi[i] = np.sum(np.abs(vel[i]*acc[i]))