# Tenemos 45 datos por cada clase, entonces seleccionaremos aleatoriamente 6 ileras de características (~15%) para  probar el algoritmo al final.

using StatsBase
# aleatorizamos los números en el rango del 1 al 45
vino_1_aleat = sample(1:45, 45, replace = false)
# aleatorizamos los números en el rango del 46 al 90
vino_2_aleat = sample(46:90, 45, replace = false)
# aleatorizamos los números en el rango del 91 al 135
vino_3_aleat = sample(91:135, 45, replace = false)

# separamos los datos que nos servirán para entrenar
x_entren = [caracteristicas[vino_1_aleat[1:39],:]; caracteristicas[vino_2_aleat[1:39],:]; caracteristicas[vino_3_aleat[1:39],:]]
y_entren = [tipo_de_vino[vino_1_aleat[1:39]]; tipo_de_vino[vino_2_aleat[1:39]]; tipo_de_vino[vino_3_aleat[1:39]]]

# separamos los datos que nos servirán para probar el algoritmo
x_prueba = [caracteristicas[vino_1_aleat[40:end],:]; caracteristicas[vino_2_aleat[40:end],:]; caracteristicas[vino_3_aleat[40:end],:]]
y_prueba = [tipo_de_vino[vino_1_aleat[40:end]]; tipo_de_vino[vino_2_aleat[40:end]]; tipo_de_vino[vino_3_aleat[40:end]]];