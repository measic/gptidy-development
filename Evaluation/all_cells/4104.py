df1 = pd.read_csv("sakamoto_daitai.csv", header=None, 
                 names=['item', 'time', 'a1_x', 'a1_y', 'a1_z', 'u1_x', 'u1_y','u1_z'])
df2 = pd.read_csv("sakamoto_katai.csv", header=None, 
                 names=['item', 'time', 'a2_x', 'a2_y', 'a2_z', 'u2_x', 'u2_y','u2_z'])