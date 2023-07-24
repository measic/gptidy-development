fig = plt.figure(figsize=(8,6)) 
x = df_county_data["Unemployment Rate"]
y = df_county_data["Graduation Rate"] 
plt.scatter(x, y, color="g", marker="o", alpha=0.9) 

#Calculate and add R2 value
mask = ~np.isnan(x) & ~np.isnan(y)


#Add regression line
sns.regplot(df_county_data["Unemployment Rate"], 
              df_county_data["Graduation Rate"], color='r',label = "Unemployment Rate" )

# Incorporate the other graph properties
plt.title("Correlation between Graduation Rates and Unemployment Rate")
plt.ylabel("Graduation Rate")
plt.xlabel("Unemployment Rate") 

plt.legend(loc='best')
plt.grid(True)
sns.set_style('whitegrid')
plt.text(12, 0.925, "Note:\nAreas with higher unemployment tend to have a lower graduation rate.")

plt.savefig("Images/County_Grad_Unemployment Rate2.png", bbox_inches = "tight")
plt.show()