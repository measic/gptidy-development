# if any of you feel like this is irrelevant plz feel free to delete it

df_county_data.boxplot("Graduation Rate", by="State", figsize=(20, 10))

plt.title("Compare Graduation Rates by States")
plt.xlabel("State")
plt.ylabel("Graduation Rate")

plt.savefig("Images/Graduation_State_Box_Plot.png", bbox_inches = "tight")
