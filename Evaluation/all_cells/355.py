#Setup Axis
state=df_county_data['State']
county = df_county_data["County Name"]
grad_rate = df_county_data["Graduation Rate"]
x_axis = np.arange(len(state))

# Create a bar chart based upon the above data
tick_locations = [value for value in x_axis]
# plt.xticks(tick_locations, county, rotation= 45)
plt.bar(x_axis, grad_rate, color="b", align="center")
plt.title("County Graduation Rates")
plt.xlabel("Counties")
plt.ylabel("Graduation Rates")
plt.text(140, 0.6, "Note:\nGraduation Rates for all counties in NJ, NY, & PA.")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Graduation_Rates.png", bbox_inches = "tight")
# plt.zoom=10
plt.show()
