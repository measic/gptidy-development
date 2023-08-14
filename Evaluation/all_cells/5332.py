dimensionalidad = 784
pixeles_por_lado = Int(sqrt(784))

# escogemos aleatoriamente un número entre 1 y 100
aleat_i = rand(1:100,1)

# inicializamos una matriz para visualizar un ejemplo de cada dígito
mat_p_vis = zeros(pixeles_por_lado*2,pixeles_por_lado*5)

# iteramos sobre los digitos (del 0 al 9) para llenar la matriz de visualización
for i=0:9

    este_digito = reshape(caracteristicas[100*i + aleat_i,:],pixeles_por_lado,pixeles_por_lado)
 
 # muy feo pero sirve para llenar la matriz que visualiza los dígitos (¡puntos extra a quien lo pueda hacer más elegantemente!)
    mat_p_vis[floor(Int,i/5)*pixeles_por_lado+1:floor(Int,i/5)*pixeles_por_lado+pixeles_por_lado,mod(i,5)*pixeles_por_lado+1:mod(i,5)*pixeles_por_lado+pixeles_por_lado] = este_digito
end

using PyPlot
imshow(mat_p_vis,cmap="Greys")