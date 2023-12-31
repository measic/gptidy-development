#Calculates correlations for stats we measured.

corr_pov = abs(df_county_data["Poverty Rate"].corr(grad_rate))
corr_hh = abs(df_county_data["Household Size"].corr(grad_rate))
corr_job = abs(df_county_data["Unemployment Rate"].corr(grad_rate))
corr_inc = abs(df_county_data["Median Income"].corr(grad_rate))
corr_ESL = abs(df_county_data["Speak a language other than English"].corr(grad_rate))

print("Correlations")
print("Poverty:             " + "{:.4f}".format(corr_pov))
print("Median Income:       " + "{:.4f}".format(corr_inc))
print("Unemployment Rates:  " + "{:.4f}".format(corr_job))
print("Non-English at Home: " + "{:.4f}".format(corr_ESL))
print("Household Size:      " + "{:.4f}".format(corr_hh))

