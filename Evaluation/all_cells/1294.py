#test bar chart for growth mean 10k 

fig = plt.figure()
fig.add_subplot()

y1 = weighted_growth10k
y2 = weighted_growth10k_18k
y3 = weighted_growth18k_32k
y4 = weighted_growth32k

x_axis = [x  for x in range(1,9)]
x_axis2 = [x + 0.2 for x in range(1,9)]
x_axis3 = [x + 0.4for x in range(1,9)]
x_axis4 = [x + 0.6 for x in range(1,9)]

plt.bar(x_axis, y1, width = 0.2, label='Tier:10k')
plt.bar(x_axis2, y2, width = 0.2, label='Growth for Tier:10k-18k')
plt.bar(x_axis3, y3, width = 0.2, label='Growth for Tier:18k-32k')
plt.bar(x_axis4, y4, width = 0.2, label='Growth for Tier: 32k')

plt.title("Tiered 'Worth-it' ratios per Region")
plt.xlabel("Region")
plt.ylabel("Worth-It Ratio")
plt.legend(title=[""])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#save fig
#plt.savefig("Plots/Worth_it.png")