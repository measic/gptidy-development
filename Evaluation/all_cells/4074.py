# Cutoff
key_quantity = len(degree_frequencies.keys())
linx = degree_frequencies.keys()[key_quantity/10:key_quantity*9/10]
loglogx = np.log(degree_frequencies.keys()[key_quantity/10:key_quantity*9/10])
loglogy = np.log(degree_frequencies.values()[key_quantity/10:key_quantity*9/10])

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(loglogx, loglogy)
print "Coeficiente de correlacion lineal Escala Log Log: " + str(r_value)
print "Error Escala Log Log: " + str(std_err)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(linx, loglogy)
print "Coeficiente de correlacion lineal Escala Semilog: " + str(r_value)
print "Error Escala Semilog: " + str(std_err)