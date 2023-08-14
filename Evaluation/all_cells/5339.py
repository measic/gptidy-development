using MAT

# obtenemos los datos que necesitamos
mnist = matread("mnist_mas.mat")
caracteristicas = mnist["cars"]
clase_de_digito = mnist["desc"];