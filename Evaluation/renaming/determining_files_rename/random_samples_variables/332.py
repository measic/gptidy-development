county = df_county_data['County Name']
variable_def = df_county_data['Household Size']
x_axis = np.arange(len(variable_def))
tick_locations = [value for value in x_axis]
plt.bar(x_axis, variable_def, color='r', align='center')
plt.title('County Household Size')
plt.xlabel('Counties')
plt.ylabel('Household Size')
plt.text(140, 2.5, 'Note:\nHousehold size for all counties in NJ, NY, & PA.')
plt.savefig('Images/County_Household_Size.png', bbox_inches='tight')
plt.show()