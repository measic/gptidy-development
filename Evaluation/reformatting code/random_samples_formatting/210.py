data_chars = []
for i, e in enumerate(data_pre):
    chars = []
    for j in range(5):
        chars.append(e[:,int(centers[i][j]-21):int(centers[i][j]+21)])
    data_chars.append(chars)