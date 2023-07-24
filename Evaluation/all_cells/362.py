fig, ax1 = plt.subplots()

tick_locations = [value for value in x_axis]

plt.xticks(tick_locations, county, rotation= 90)

grad_rate = df_county_data["Graduation Rate"]
county = df_county_data["County Name"]
pov_rate = df_county_data["Household Size"]
t = np.arange(len(county))
ax1.plot(t, pov_rate, 'b-')
ax1.set_xlabel('county')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('HouseHold Size', color='b')
ax1.tick_params('y', colors='b')
plt.title("High School Graduation Rates and Household Size by County")
ax2 = ax1.twinx()

ax2.plot(t,grad_rate, 'r*')
ax2.set_ylabel('Graduation Rate', color='r')
ax2.tick_params('y', colors='r')
zoom = 5
w, h = fig.get_size_inches()
fig.set_size_inches(w * zoom, h * zoom/2)
fig.tight_layout()
plt.savefig("Images/County_Grad_House_Rates1.png", bbox_inches = "tight")
plt.show()