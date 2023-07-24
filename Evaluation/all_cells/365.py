grad_rate = df_county_data["Graduation Rate"]
house_size = df_county_data["Unemployment Rate"]

plt.scatter(house_size, grad_rate)

plt.grid()
plt.title("High School Graduation Rates and Unemployment Rate by County")
plt.ylabel("Graduation Rates")
plt.xlabel("Unemployment Rate")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Grad_Unemployment_Rates.png", bbox_inches = "tight")
plt.show()