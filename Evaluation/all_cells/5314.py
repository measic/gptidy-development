# instalamos un paquete de Julia para poder obtener los datos
Pkg.add("MAT") 
using MAT

# obtenemos los datos que necesitamos
iris = matread("iris.mat")
caracteristicas = iris["meas"]
especies = iris["species"];