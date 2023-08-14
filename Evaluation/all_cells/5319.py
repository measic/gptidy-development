# generamos una variable con las dos características que nos interesan
x = [caracteristicas[:,1] caracteristicas[:,2]]

# obtenemos las características globales promedio
x_prom = mean(x,1)

# extraemos las caracteristicas globales promedio de nuestros datos
x = x - x_prom.*ones(150,2)

# graficamos nuevamente
scatter(x[1:50,1],x[1:50,2], color="b")
scatter(x[51:100,1],x[51:100,2], color="r")
scatter(x[101:150,1],x[101:150,2], color="g")
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")
grid("on")