county = df_county_data['County Name']
pov_rate = df_county_data['Poverty Rate']
x_axis = np.arange(len(pov_rate))
variable_def = [value for value in x_axis]
plt.bar(x_axis, pov_rate, color='r', align='center')
plt.title('County Poverty Rates')
plt.xlabel('Counties')
plt.ylabel('Poverty Rates')
plt.text(140, 30, 'Note:\nPoverty Rates for all counties in NJ, NY, & PA.')
plt.savefig('Images/County_Poverty_Rates.png', bbox_inches='tight')
plt.show()