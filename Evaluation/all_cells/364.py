county = df_county_data["County Name"]
house_size = df_county_data["Unemployment Rate"]
x_axis = np.arange(len(house_size))
# Create a bar chart based upon the above data
tick_locations = [value for value in x_axis]
# plt.xticks(tick_locations, county, rotation= 90)
plt.bar(x_axis, house_size, color="r", align="center")
plt.title("County Unemployment Rate")
plt.xlabel("Counties")
plt.ylabel("Unemployment Rate")
plt.text(140, 7, "Note:\nUnemployment Rates for all counties in NJ, NY, & PA.")
# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Unemployment1.png", bbox_inches = "tight")
plt.show()