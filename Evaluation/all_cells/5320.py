# graficamos las dos características que más sirven para diferenciar las especies de flores.
scatter(caracteristicas[1:50,1],caracteristicas[1:50,2], color="b")
scatter(caracteristicas[51:100,1],caracteristicas[51:100,2], color="r")
scatter(caracteristicas[101:150,1],caracteristicas[101:150,2], color="g")
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")