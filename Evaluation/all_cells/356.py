county = df_county_data["County Name"]
pov_rate = df_county_data["Poverty Rate"]
x_axis = np.arange(len(pov_rate))
# Create a bar chart based upon the above data
tick_locations = [value for value in x_axis]
# plt.xticks(tick_locations, county, rotation= 90)
plt.bar(x_axis, pov_rate, color="r", align="center")
plt.title("County Poverty Rates")
plt.xlabel("Counties")
plt.ylabel("Poverty Rates")
plt.text(140, 30, "Note:\nPoverty Rates for all counties in NJ, NY, & PA.")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Poverty_Rates.png", bbox_inches = "tight")
plt.show()