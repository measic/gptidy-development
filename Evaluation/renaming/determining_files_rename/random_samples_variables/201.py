fig = plt.figure()
fig.add_subplot()
y1 = earningsgrowth10k
y2 = earningsgrowth10k_18k
y3 = earningsgrowth18k_32k
y4 = earningsgrowth32kk
x_axis = [x for x in range(1, 9)]
x_axis2 = [x + 0.2 for x in range(1, 9)]
x_axis3 = [x + 0.4 for x in range(1, 9)]
variable_def = [x + 0.6 for x in range(1, 9)]
plt.bar(x_axis, y1, width=0.2, label='Growth for Tier:10k')
plt.bar(x_axis2, y2, width=0.2, label='Growth for Tier:10k-18k')
plt.bar(x_axis3, y3, width=0.2, label='Growth for Tier:18k-32k')
plt.bar(variable_def, y4, width=0.2, label='Growth for Tier: 32k')
plt.title('Earnings Growth years 6-10')
plt.xlabel('Region')
plt.ylabel('Earnings Growth')
plt.legend(title=['Earnings Growth years 6-10'])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)