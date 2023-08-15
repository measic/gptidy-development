# obtenemos los datos que necesitamos y los ponemos en una matriz de Julia
vinos = matread("wine.mat")
datos = vinos["data"]

# separamos las caracteristicas y los tipos de vino
caracteristicas = datos[:,2:end]
tipo_de_vino = datos[:,1];