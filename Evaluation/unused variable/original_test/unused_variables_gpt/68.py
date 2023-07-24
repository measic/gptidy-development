fig = plt.figure(figsize=(8,6)) 
x = df_county_data["Speak a language other than English"]
y = df_county_data["Graduation Rate"] 
plt.scatter(x, y, color="g", marker="o", alpha=0.9) 

#Calculate and add R2 value
mask = ~np.isnan(x) & ~np.isnan(y)

#Add regression line
sns.regplot(df_county_data["Speak a language other than English"], 
              df_county_data["Graduation Rate"], color='r',label = "Speak a language other than English" )

# Incorporate the other graph properties
plt.title("High School Graduation Rates and ESL by County")
plt.ylabel("Graduation Rate")
plt.xlabel("Speak a language other than English") 

plt.legend(loc='best')
plt.grid(True)
sns.set_style('whitegrid')
plt.text(65, 0.925, "Note:\nAreas with one or more Foreign languages beside English language \ntend to have a Lower graduation rate.")

plt.savefig("Images/County_Grad_Speak a language other than English3.png", bbox_inches = "tight")
plt.show()