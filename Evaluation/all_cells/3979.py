statinfo = os.stat(pickle_file)
print('Compressed pickle size:', statinfo.st_size)