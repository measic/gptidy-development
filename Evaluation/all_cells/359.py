fig = plt.figure(figsize=(8,6)) 
x = df_county_data["Poverty Rate"] 
y = df_county_data["Graduation Rate"] 
plt.scatter(x, y, color="g", marker="o", alpha=0.9) 

#Calculate and add R2 value
mask = ~np.isnan(x) & ~np.isnan(y)


#Add regression line
sns.regplot(df_county_data["Poverty Rate"], 
              df_county_data["Graduation Rate"], color='r',label = "Poverty " )

# Incorporate the other graph properties
plt.title("Correlation between Graduation rates and Poverty rates")
plt.ylabel("Graduation rate")
plt.xlabel("Poverty rate") 

plt.legend(loc='best')
plt.grid(True)
sns.set_style('whitegrid')
plt.text(50, 0.925, "Note:\nWe notice an inverse corellation ship between Graduation rates and Povetry rates.")

plt.savefig("Images/County_Grad_Poverty_Rates3.png", bbox_inches = "tight")
plt.show()