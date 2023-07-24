fig = plt.figure(figsize=(8,6)) 
x = df_county_data["Household Size"]
y = df_county_data["Graduation Rate"] 
plt.scatter(x, y, color="g", marker="o", alpha=0.9) 

#Calculate and add R2 value
mask = ~np.isnan(x) & ~np.isnan(y)


#Add regression line
sns.regplot(df_county_data["Household Size"], 
              df_county_data["Graduation Rate"], color='r',label = "Household Size" )

# Incorporate the other graph properties
plt.title("Correlation between Graduation rates and Household Size")
plt.ylabel("Graduation Rate")
plt.xlabel("House Size") 

plt.legend(loc='best')
plt.grid(True)
sns.set_style('whitegrid')
plt.text(3.4, 0.925, "Note:\nThere is a slight inverse correlation shown in this graph.")

plt.savefig("Images/County_Grad_House_Rates2.png", bbox_inches = "tight")
plt.show()