# escogemos aleatoriamente una ilera en los datos
ilera_al = rand(1:150,1)

# extraemos los datos de esta ilera en una variable nueva
x_muestra = x[ilera_al,:]

# calculamos el producto interno de esta muestra con cada uno de los vectores promedio
prod_1 = x_muestra*prom_1'
prod_2 = x_muestra*prom_2'
prod_3 = x_muestra*prom_3'

# imprimimos los resultados
print("el producto interno del vector muestra con de los vectores promedio correspondientes a las especies de plantas son: \n")
print("\n setosa ", prod_1)
print("\n versicolor ", prod_2)
print("\n virginica ", prod_3)
print("\n\ny la especie correcta del vector muestra es: \n")
print("\n ", especies[ilera_al])