grad_rate = df_county_data["Graduation Rate"]
house_size = df_county_data["Household Size"]

plt.scatter(house_size, grad_rate)

plt.grid()
plt.title("High School Graduation Rates and Household Size by County")
plt.ylabel("Graduation Rates")
plt.xlabel("Household Size")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Grad_House_Rates.png", bbox_inches = "tight")
plt.show()