using StatsBase

# separamos los datos que nos servirán para entrenar
x_entren = [
    caracteristicas[dig_0_aleat[1:950],:];
    caracteristicas[dig_1_aleat[1:950],:];
    caracteristicas[dig_2_aleat[1:950],:];
    caracteristicas[dig_3_aleat[1:950],:];
    caracteristicas[dig_4_aleat[1:950],:];
    caracteristicas[dig_5_aleat[1:950],:];
    caracteristicas[dig_6_aleat[1:950],:];
    caracteristicas[dig_7_aleat[1:950],:];
    caracteristicas[dig_8_aleat[1:950],:];
    caracteristicas[dig_9_aleat[1:950],:];
]
y_entren = [
    clase_de_digito[dig_0_aleat[1:950],:];
    clase_de_digito[dig_1_aleat[1:950],:];
    clase_de_digito[dig_2_aleat[1:950],:];
    clase_de_digito[dig_3_aleat[1:950],:];
    clase_de_digito[dig_4_aleat[1:950],:];
    clase_de_digito[dig_5_aleat[1:950],:];
    clase_de_digito[dig_6_aleat[1:950],:];
    clase_de_digito[dig_7_aleat[1:950],:];
    clase_de_digito[dig_8_aleat[1:950],:];
    clase_de_digito[dig_9_aleat[1:950],:];
]


# separamos los datos que nos servirán para probar
x_prueba = [
    caracteristicas[dig_0_aleat[951:end],:];
    caracteristicas[dig_1_aleat[951:end],:];
    caracteristicas[dig_2_aleat[951:end],:];
    caracteristicas[dig_3_aleat[951:end],:];
    caracteristicas[dig_4_aleat[951:end],:];
    caracteristicas[dig_5_aleat[951:end],:];
    caracteristicas[dig_6_aleat[951:end],:];
    caracteristicas[dig_7_aleat[951:end],:];
    caracteristicas[dig_8_aleat[951:end],:];
    caracteristicas[dig_9_aleat[951:end],:];
]
y_prueba = [
    clase_de_digito[dig_0_aleat[951:end],:];
    clase_de_digito[dig_1_aleat[951:end],:];
    clase_de_digito[dig_2_aleat[951:end],:];
    clase_de_digito[dig_3_aleat[951:end],:];
    clase_de_digito[dig_4_aleat[951:end],:];
    clase_de_digito[dig_5_aleat[951:end],:];
    clase_de_digito[dig_6_aleat[951:end],:];
    clase_de_digito[dig_7_aleat[951:end],:];
    clase_de_digito[dig_8_aleat[951:end],:];
    clase_de_digito[dig_9_aleat[951:end],:];
]

# removemos las caracteristicas globales promedio de x_entren y x_prueba
x_prom = mean(x_entren,1)

x_entren = x_entren - x_prom.*ones(size(x_entren))
x_prueba = x_prueba - x_prom.*ones(size(x_prueba))