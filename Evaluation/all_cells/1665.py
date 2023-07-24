with open(data_path + '/power_data.pickle', 'wb') as file:
    pickle.dump(power_data_synced, file)
    file.close()