# graficamos la longitud de pétalo para el primer tipo de flores
figure(1)
scatter(0.1*randn(50,1),caracteristicas[1:50,1])
scatter(1+0.1*randn(50,1),caracteristicas[51:100,1])
scatter(2+0.1*randn(50,1),caracteristicas[101:150,1])
ylabel("Longitud del Pétalo (cm)")

# graficamos la anchura del pétalo
figure(2)

# graficamos la longitud del sépalo
figure(3)

# graficamos la anchura del sépalo
figure(4)