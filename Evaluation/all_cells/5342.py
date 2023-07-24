using StatsBase

# aleatorizamos los indices de las ileras que corresponden a cada dígito
dig_0_aleat = sample(1:1000, 1000, replace = false)
dig_1_aleat = sample(1001:2000, 1000, replace = false)
dig_2_aleat = sample(2001:3000, 1000, replace = false)
dig_3_aleat = sample(3001:4000, 1000, replace = false)
dig_4_aleat = sample(4001:5000, 1000, replace = false)
dig_5_aleat = sample(5001:6000, 1000, replace = false)
dig_6_aleat = sample(6001:7000, 1000, replace = false)
dig_7_aleat = sample(7001:8000, 1000, replace = false)
dig_8_aleat = sample(8001:9000, 1000, replace = false)
dig_9_aleat = sample(9001:10000, 1000, replace = false)

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
x_prueba = x_prueba - x_prom.*ones(size(x_prueba));