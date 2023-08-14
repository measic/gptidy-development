fig_size= plt.rcParams["figure.figsize"]

# Set figure width to 12 and height to 9
fig_size[0] = 22
fig_size[1] = 7
plt.rcParams["figure.figsize"] = fig_size

print ("Current size:",fig_size)
