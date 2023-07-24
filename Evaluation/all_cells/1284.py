x_axis = [x for x in range(1,9)]
y_axis = mean_df_clean["earnings_cost_ratio"]

plt.plot(x_axis, y_axis, 'go--', linewidth=2, markersize=8, color='blue', label="Earning-Cost Ratio")

plt.title("Earnings/Cost ratio per region ($)")
plt.xlabel("Region")
plt.ylabel("Earnings/Cost Ratio")
plt.grid()
plt.legend(title=[""])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#save fig
#plt.savefig("Plots/Earnings-CostRatioPerRegion.png")