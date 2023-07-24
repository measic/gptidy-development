grad_rate = df_county_data["Graduation Rate"]
house_size = df_county_data["Speak a language other than English"]

plt.scatter(house_size, grad_rate)

plt.grid()
plt.title("High School Graduation Rates and ESL by County")
plt.ylabel("Graduation Rates")
plt.xlabel("Speak a language other than English")

# Save an image of the chart and print it to the screen
plt.savefig("Images/County_Grad_Speak a language other than English1.png", bbox_inches = "tight")
plt.show()