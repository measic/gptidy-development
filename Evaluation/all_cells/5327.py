### 1. tu código aquí para substraer el promedio global a todos los datos ###
# obtenemos las características globales promedio
x_prom = 

# extraemos las caracteristicas globales promedio de nuestros datos
x_entren = 

### 2. tu código aquí para encontrar las características promedio para cada tipo de vino ###
prom_1 = 
prom_2 = 
prom_3 = 

# el siguiente código va a graficar los datos y las características promedio
scatter3D(x_entren[1:39,1],x_entren[1:39,2],x_entren[1:39,3], alpha = 0.25, color="b")
scatter3D(prom_1[1,1],prom_1[1,2],prom_1[1,3], s = 100, color="b")
scatter3D(x_entren[40:78,1],x_entren[40:78,2],x_entren[40:78,3], alpha = 0.25, color="r")
scatter3D(prom_2[1,1],prom_2[1,2],prom_2[1,3], s = 100, color="r")
scatter3D(x_entren[79:end,1],x_entren[79:end,2],x_entren[79:end,3], alpha = 0.25, color="g")
scatter3D(prom_3[1,1],prom_3[1,2],prom_3[1,3], s = 100,color="g")
xlabel("Contenido de Alcohol")
ylabel("Contenido de Flavonoides")
zlabel("Densidad Optica Relativa")