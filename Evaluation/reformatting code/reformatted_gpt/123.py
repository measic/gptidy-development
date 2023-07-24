# Extract a column from dataframe df3
nums = df3['y']
print(nums)
print(type(nums))

# Convert to a numpy array
realnums = np.array(nums)
print('After conversion')
print(type(realnums))
print(realnums)