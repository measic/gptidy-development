import csv
import datetime
import os
import glob
variable_def = '/home/ivan/Área de trabalho/2017'
lista = []
for filename in glob.iglob(variable_def + '**/*/*/*/*stamp.jpg*', recursive=True):
    lista.append(filename)
print(lista[:4])
print(len(lista))
print(find_conteiner(lista[1]))
print(find_conteiner(lista[15]))