county = df_county_data['County Name']
house_size = df_county_data['Speak a language other than English']
x_axis = np.arange(len(house_size))
variable_def = [value for value in x_axis]
plt.bar(x_axis, house_size, color='r', align='center')
plt.title('County ESL')
plt.xlabel('Counties')
plt.ylabel('Speak a language other than English')
plt.text(140, 40, 'Note:\nSpoken languages beside English for all counties in NJ, NY, & PA.')
plt.savefig('Images/County_Speak a language other than English.png', bbox_inches='tight')
plt.show()