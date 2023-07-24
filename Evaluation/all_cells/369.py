grad_rate = df_county_data["Graduation Rate"]
house_size = df_county_data["Median Income"]

plt.scatter(house_size, grad_rate)

plt.grid()
plt.title("High School Graduation Rates and Median Income by County")
plt.ylabel("Graduation Rates")
plt.xlabel("Median Income")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Grad_Median Income1.png", bbox_inches = "tight")
plt.show()