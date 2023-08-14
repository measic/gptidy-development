# graficamos los datos nuevamente
scatter(x[1:50,1],x[1:50,2],alpha=0.25, color="b")
scatter(x[51:100,1],x[51:100,2],alpha=0.25, color="r")
scatter(x[101:150,1],x[101:150,2],alpha=0.25, color="g")
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")
grid("on")

# obtenemos los vectores con las características promedio para cada una de las clases de flores
prom_1 = mean(x[1:50,:],1)
prom_2 = mean(x[51:100,:],1)
prom_3 = mean(x[101:150,:],1)

# graficamos los vectores
quiver(prom_1[1,1],prom_1[1,2],angles="xy", scale_units="xy", scale=1, color="b")
quiver(prom_2[1,1],prom_2[1,2],angles="xy", scale_units="xy", scale=1, color="r")
quiver(prom_3[1,1],prom_3[1,2],angles="xy", scale_units="xy", scale=1, color="g")