x2 = 25
y2 = -25.7
z2 = 'World'
data2 = np.array([13, 15, 17])
# note that we have to make the numpy array into a list with the [] so it is the initialization knows it is
# to go into a single cell.
row1 = {'x': x, 'y': y, 'z': z, 'data': [data]}
row2 = {'x': x2, 'y': y2, 'z': z2, 'data': data2}

df3 = pd.DataFrame(row1)
df3 = df3.append(row2, ignore_index=True)
print(df3)