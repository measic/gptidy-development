fig = plt.figure(figsize=(8,6)) 
x = df_county_data["Median Income"]
y = df_county_data["Graduation Rate"] 
plt.scatter(x, y, color="g", marker="o", alpha=0.9) 

#Calculate and add R2 value
mask = ~np.isnan(x) & ~np.isnan(y)


#Add regression line
sns.regplot(df_county_data["Median Income"], 
              df_county_data["Graduation Rate"], color='r',label = "Median Income" )

# Incorporate the other graph properties
plt.title("Correlation between Graduation rates and Median Income")
plt.ylabel("Graduation rate")
plt.xlabel("Median Income") 

plt.legend(loc='best')
plt.grid(True)
sns.set_style('whitegrid')
plt.text(170000, 0.925, "Note:\nAreas with higher median income tend to have a higher graduation rate.")

plt.savefig("Images/County_Grad_Median Income3.png", bbox_inches = "tight")
plt.show()