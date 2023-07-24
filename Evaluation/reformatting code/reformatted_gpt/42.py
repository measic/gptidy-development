f = open(p_data)

data = []
for line in f:
    data_line = line.rstrip().split('\t')
    data.append(data_line)

init = True
for i, file in enumerate(data[9:]):
    file = file[0].replace(',', '.')
    file = file.replace(' ', '')
    if init:
        Volt_Amp_data = np.ndarray((len(data), len(file.split(';')) - 1))
        init = False
    Volt_Amp_data[i] = np.array([float(n) for n in file.split(';')[:len(file.split(';')) - 1]])