plt.loglog(degree_frequencies.keys(), degree_frequencies.values(), basex=np.e, basey=np.e)
plt.title("Cantidad de autores de cada grado - Escala Log Log")
plt.show()