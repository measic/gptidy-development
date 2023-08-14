using MAT

# obtenemos los datos que necesitamos
mnist = matread("cifar_10.mat")
caracteristicas = mnist["imag"]
clase_de_digito = floor(Int,mnist["desc"])

# visualización de un ejemplo al azar
ind_aleat = sample(1:size(caracteristicas)[1],1)
using PyPlot
imshow(reshape(caracteristicas[ind_aleat,:],32,32,3))