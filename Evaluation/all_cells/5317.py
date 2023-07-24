# instalamos un paquete de Julia para poder visualizar los datos
Pkg.add("PyPlot")
using PyPlot

# graficamos la longitud de pétalo para el primer tipo de flores
scatter(0.1*randn(50,1),caracteristicas[1:50,1])
# agregamos la longitud de pétalo para el segundo tipo de flores
scatter(1+0.1*randn(50,1),caracteristicas[51:100,1])
# agregamos la longitud de pétalo para el tercer tipo de flores
scatter(2+0.1*randn(50,1),caracteristicas[101:150,1])
ylabel("Longitud del Pétalo (cm)")