
x_axis = ["Poverty", "Med Inc", "Unemployment", "ESL", "HH Size"]
y_axis = [corr_pov, corr_inc, corr_job, corr_ESL, corr_hh]

plt.bar(x_axis, y_axis, color="b", align="center")
plt.title("Correlations of Demographic Metrics to High School Graduation Rates")
plt.xlabel("Demographic Metric")
plt.ylabel("Correlation")


plt.show()
