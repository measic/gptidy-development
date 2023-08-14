variable_def = [x for x in range(1, 9)]
y_axis1 = df0_10k_grouped['earnings_cost_ratio']
y_axis2 = df10_18k_grouped['earnings_cost_ratio']
y_axis3 = df18_32_grouped['earnings_cost_ratio']
y_axis4 = df32_grouped['earnings_cost_ratio']
lessThan10k = plt.plot(variable_def, y_axis1, 'go--', linewidth=2, markersize=8, color='blue', label='lessThan10k')
TenKto18k = plt.plot(variable_def, y_axis2, 'go--', linewidth=2, markersize=8, color='green', label='10Kto18k')
EighteenTo32k = plt.plot(variable_def, y_axis3, 'go--', linewidth=2, markersize=8, color='yellow', label='18kTo32k')
greaterThan32k = plt.plot(variable_def, y_axis4, 'go--', linewidth=2, markersize=8, color='red', label='>32k')
plt.title('Tiered Earnings-Cost ratio per region ($)')
plt.xlabel('Region')
plt.ylabel('Tiered Earnings-cost Ratio')
plt.grid()
plt.legend(title=['Tiered Tuitions'])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)