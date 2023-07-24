grad_rate = df_county_data["Graduation Rate"]
pov_rate = df_county_data["Poverty Rate"]

plt.scatter(pov_rate, grad_rate)

plt.grid()
plt.title("High School Graduation Rates and Poverty Rates by County")
plt.ylabel("Graduation Rates")
plt.xlabel("Poverty Rate")
# plt.text(50, 0.925, "Note:\nWe notice an inverse corellation ship between Graduation rates and Povetry rates.")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Grad_Poverty_Rates1.png", bbox_inches = "tight")
plt.show()