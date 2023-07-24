#Path to the different folders
data_path = 'data'
temp_path = data_path + '/temp'
backup_path = data_path + '/backup'

if not os.path.isdir(data_path):
    os.mkdir(data_path)
    os.mkdir(temp_path)
    os.mkdir(backup_path)