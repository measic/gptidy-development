#average (region, tuition) & (region, earnings6years)
y1 = mean_df_clean["tuition_in_state"]
y2 = mean_df_clean["earnings6years"]

x_axis = [x for x in range(1,9)]
x_axis2 = [x+0.3 for x in range(1,9)]

plt.bar(x_axis, y1, width = 0.3, label="Tuition" )
plt.bar(x_axis2, y2, width = 0.3, label="Earnings")

plt.title("Tuition and Earnings per Region")
plt.xlabel("Region")
plt.ylabel("Average Tuition & Earnings ($)")
plt.legend(title=["Legend"])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#save fig
#plt.savefig("Plots/Tuition&EarningsPerRegion.png")