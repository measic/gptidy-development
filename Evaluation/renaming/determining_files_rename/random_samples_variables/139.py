fig, ax1 = plt.subplots()
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, county, rotation=90)
grad_rate = df_county_data['Graduation Rate']
county = df_county_data['County Name']
pov_rate = df_county_data['Speak a language other than English']
t = np.arange(len(county))
ax1.plot(t, pov_rate, 'b-')
ax1.set_xlabel('county')
ax1.set_ylabel('Speak a language other than English', color='b')
ax1.tick_params('y', colors='b')
plt.title('High School Graduation Rates and ESL by County')
variable_def = ax1.twinx()
variable_def.plot(t, grad_rate, 'r*')
variable_def.set_ylabel('Graduation Rate', color='r')
variable_def.tick_params('y', colors='r')
zoom = 5
w, h = fig.get_size_inches()
fig.set_size_inches(w * zoom, h * zoom / 2)
fig.tight_layout()
plt.savefig('Images/County_Grad_Speak a language other than English2.png', bbox_inches='tight')
plt.show()