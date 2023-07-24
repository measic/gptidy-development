import csv
import datetime
import os
import glob

IMG_PATH = '/home/ivan/Área de trabalho/2017'

lista = []
for filename in glob.iglob(IMG_PATH + '**/*/*/*/*stamp.jpg*', recursive=True):
    lista.append(filename)

print(lista[:4])
print(len(lista))
print(find_conteiner(lista[1]))
print(find_conteiner(lista[15]))