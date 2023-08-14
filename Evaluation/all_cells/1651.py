with open(a_data, 'r') as file:
    try:
        data = file.read()
        file.close()
    except UnicodeDecodeError:
        file.close()
data = data.splitlines()
data = data[4:len(data)-1] #Text information on first four rows and END on last row

data_dim = len(data[0].split()[1:])

traj_data = np.ndarray((len(data),data_dim))
for i, row in enumerate(data):
    traj_data[i] = np.array([float(n)*np.pi/180 for n in row.split()[1:]])

with open(data_path + '/joint_angle_data.pickle', 'wb') as file:
    pickle.dump(traj_data, file)
    file.close()